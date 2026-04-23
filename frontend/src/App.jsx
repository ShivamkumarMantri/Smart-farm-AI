import { useState, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import './index.css';

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [cropName, setCropName] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    handleFile(e.dataTransfer.files[0]);
  };

  const handleChange = (e) => {
    handleFile(e.target.files[0]);
  };

  const handleFile = (selectedFile) => {
    if (selectedFile && selectedFile.type.startsWith('image/')) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
      setResult(null);
      setError(null);
    }
  };

  const triggerSelect = () => {
    fileInputRef.current.click();
  };

  const analyze = async () => {
    if (!file) return;
    setLoading(true);
    setError(null);
    
    const formData = new FormData();
    formData.append('file', file);
    if (cropName.trim() !== "") {
      formData.append('userCrop', cropName);
    }
    // We can add forceGemini: true if needed by appending 'forceGemini': 'true'

    try {
      const response = await fetch('http://localhost:8000/api/predict', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      
      if (data.success) {
        setResult(data.result);
      } else {
        setError(data.error || "An error occurred during analysis.");
      }
    } catch (err) {
      setError("Failed to connect to the backend server. Is FastAPI running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="flex-center" style={{ marginBottom: '2rem' }}>
        <h1 className="title">🌾 SmartFarm AI</h1>
        <p className="subtitle">Advanced Pathological Intelligence for Sustainable Farming</p>
      </div>

      <div className="grid">
        {/* Left Column - Input */}
        <div className="glass-panel">
          <h2>1. Upload Lead Image</h2>
          {!preview ? (
            <div 
              className="upload-area"
              onDragOver={handleDragOver}
              onDrop={handleDrop}
              onClick={triggerSelect}
            >
              <i>📸</i>
              <h3>Drag & Drop your plant leaf here</h3>
              <p style={{ color: 'var(--text-dark)' }}>or click to browse files (JPEG, PNG)</p>
              <input 
                type="file" 
                ref={fileInputRef} 
                onChange={handleChange} 
                accept="image/*"
              />
            </div>
          ) : (
            <div style={{ textAlign: 'center' }}>
              <img src={preview} alt="Leaf Preview" className="img-preview" />
              <button 
                onClick={() => { setFile(null); setPreview(null); setResult(null); }}
                style={{ background: 'transparent', color: 'var(--secondary)', border: '1px solid var(--secondary)', cursor: 'pointer', padding: '0.5rem 1rem', borderRadius: '8px', marginBottom: '1rem' }}
              >
                Change Image
              </button>
            </div>
          )}

          <div style={{ marginTop: '2rem' }}>
            <h3>Optional: Crop Context</h3>
            <input 
              type="text" 
              placeholder="e.g. Tomato, Potato (leave blank for auto-detect)"
              value={cropName}
              onChange={(e) => setCropName(e.target.value)}
            />
            
             <button className="btn" onClick={analyze} disabled={!file || loading}>
               {loading ? (
                 <>
                   <div className="spinner" style={{ width: '20px', height: '20px', borderWidth: '2px', verticalAlign: 'middle', marginRight: '10px', marginBottom: '0' }}></div>
                   Analyzing...
                 </>
               ) : '🔍 Analyze Health'}
             </button>
          </div>
        </div>

        {/* Right Column - Processing & Result */}
        <div className="glass-panel" style={{ minHeight: '500px' }}>
          <h2>2. Diagnosis Results</h2>
          
          {!result && !loading && !error && (
            <div className="flex-center" style={{ height: '70%', color: 'var(--text-dark)' }}>
              <i>✨</i>
              <p>Upload a photo and click analyze to view AI diagnostics.</p>
            </div>
          )}

          {loading && (
             <div className="flex-center" style={{ height: '70%' }}>
               <div className="spinner"></div>
               <p style={{ marginTop: '1rem', color: 'var(--secondary)' }}>Our Neural Network is evaluating your image...</p>
             </div>
          )}

          {error && (
            <div style={{ padding: '1rem', backgroundColor: 'rgba(239, 68, 68, 0.2)', border: '1px solid #ef4444', borderRadius: '12px', color: '#fca5a5' }}>
              ⚠️ {error}
            </div>
          )}

          {result && (
            <div className="fadeIn">
              <span className="badge">Mode: {result.stage === 'cached_result' ? '⚡ Memory Cache' : (result.stage.includes('gemini') ? '🧬 Deep Vision Analysis' : '🧠 Standard CNN')}</span>
              
              {result.metadata && result.metadata.cnn_conf && (
                <div style={{ float: 'right', fontSize: '0.9rem', color: 'var(--text-dark)' }}>
                  Confidence: <strong style={{ color: 'var(--primary)' }}>{(result.metadata.cnn_conf * 100).toFixed(1)}%</strong>
                </div>
              )}
              
              <div className="markdown-body" style={{ marginTop: '1rem' }}>
                <ReactMarkdown>{result.message}</ReactMarkdown>
              </div>
            </div>
          )}
        </div>
      </div>
      
      <div style={{ textAlign: 'center', marginTop: '4rem', color: 'var(--text-dark)', fontSize: '0.9rem' }}>
        <p>🌿 SmartFarm AI 2025-26 | Developed by Team SmartFarm</p>
      </div>
    </div>
  );
}

export default App;
