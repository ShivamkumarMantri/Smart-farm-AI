"""
services/weather_service.py
------------------------------------------------------------
Free weather data using Open-Meteo API (no API key needed).
Provides current conditions + 24h forecast for LLM context.
"""
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

def get_weather(city: str) -> Optional[Dict[str, Any]]:
    """
    Fetch current weather for a city using Open-Meteo (free, no key).
    Returns a dict with temperature, humidity, rain, wind, and a text summary.
    Returns None on any failure — caller should handle gracefully.
    """
    try:
        import requests

        # Step 1: Geocode city → lat/lon
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_resp = requests.get(geo_url, params={"name": city, "count": 1, "language": "en", "format": "json"}, timeout=5)
        geo_data = geo_resp.json()

        if not geo_data.get("results"):
            logger.warning("City not found: %s", city)
            return None

        result = geo_data["results"][0]
        lat, lon = result["latitude"], result["longitude"]
        location_name = f"{result.get('name', city)}, {result.get('country', '')}"

        # Step 2: Fetch current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat, "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m", "weather_code"],
            "daily": ["precipitation_sum", "temperature_2m_max", "temperature_2m_min"],
            "timezone": "auto", "forecast_days": 2,
        }
        w_resp = requests.get(weather_url, params=params, timeout=5)
        w = w_resp.json()

        current = w.get("current", {})
        daily   = w.get("daily", {})

        temp     = current.get("temperature_2m", "N/A")
        humidity = current.get("relative_humidity_2m", "N/A")
        rain     = current.get("precipitation", 0)
        wind     = current.get("wind_speed_10m", "N/A")
        code     = current.get("weather_code", 0)

        # Tomorrow's rain forecast
        tomorrow_rain = daily.get("precipitation_sum", [0, 0])[1] if daily.get("precipitation_sum") else 0
        tomorrow_max  = daily.get("temperature_2m_max", ["N/A", "N/A"])[1]

        # Human-readable condition
        condition = _wmo_to_condition(code)

        summary = (
            f"Location: {location_name}\n"
            f"Current: {condition}, {temp}°C, Humidity: {humidity}%\n"
            f"Wind: {wind} km/h, Current Rainfall: {rain} mm\n"
            f"Tomorrow forecast: Max {tomorrow_max}°C, Rain: {tomorrow_rain} mm"
        )

        return {
            "location": location_name,
            "temp": temp,
            "humidity": humidity,
            "rain": rain,
            "wind": wind,
            "condition": condition,
            "tomorrow_rain": tomorrow_rain,
            "summary": summary,
        }

    except Exception as e:
        logger.warning("Weather fetch failed for '%s': %s", city, e)
        return None


def _wmo_to_condition(code: int) -> str:
    """Convert WMO weather code to human-readable string."""
    mapping = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Icy fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Heavy drizzle",
        61: "Light rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Light snow", 73: "Moderate snow", 75: "Heavy snow",
        80: "Light showers", 81: "Moderate showers", 82: "Heavy showers",
        95: "Thunderstorm", 96: "Thunderstorm with hail",
    }
    return mapping.get(code, f"Weather code {code}")


def weather_farming_advice(weather: Dict[str, Any]) -> str:
    """
    Generate a brief weather-based farming tip string to inject into LLM prompts.
    """
    tips = []
    humidity = weather.get("humidity", 0)
    rain     = weather.get("rain", 0)
    tomorrow = weather.get("tomorrow_rain", 0)
    temp     = weather.get("temp", 20)

    if isinstance(humidity, (int, float)) and humidity > 80:
        tips.append("High humidity (>80%) increases fungal disease risk — avoid overhead watering.")
    if isinstance(rain, (int, float)) and rain > 2:
        tips.append("It is currently raining — delay spraying fungicides until conditions are dry.")
    elif isinstance(tomorrow, (int, float)) and tomorrow > 5:
        tips.append(f"Rain forecast tomorrow ({tomorrow} mm) — apply any chemical treatments TODAY before rain.")
    else:
        tips.append("No significant rain in the next 24 hours — a good window for applying sprays.")
    if isinstance(temp, (int, float)) and temp > 35:
        tips.append("High temperature (>35°C) — apply treatments in the early morning or evening to avoid leaf burn.")

    return " | ".join(tips) if tips else "Conditions are generally suitable for standard treatment."
