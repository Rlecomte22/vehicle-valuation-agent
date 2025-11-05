import React, { useState } from 'react';

export default function ValuationForm() {
  const [vin, setVin] = useState('');
  const [mileage, setMileage] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const API_BASE = import.meta.env.VITE_API_BASE || 'https://valuation-api.onrender.com';

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch(`${API_BASE}/value`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ vin, mileage: mileage ? Number(mileage) : null }),
      });
      if (!res.ok) throw new Error(`API error ${res.status}`);
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const downloadReport = () => {
    const url = `${API_BASE}/report/${encodeURIComponent(vin)}`;
    window.open(url, '_blank');
  };

  return (
    <div className="bg-white p-6 rounded-xl shadow-md w-full max-w-md">
      <form onSubmit={handleSubmit} className="flex flex-col gap-3">
        <input
          type="text"
          value={vin}
          onChange={(e) => setVin(e.target.value)}
          placeholder="Enter VIN"
          className="border p-2 rounded"
          required
        />
        <input
          type="number"
          value={mileage}
          onChange={(e) => setMileage(e.target.value)}
          placeholder="Mileage (optional)"
          className="border p-2 rounded"
        />
        <button type="submit" className="bg-blue-600 text-white rounded p-2 disabled:opacity-60" disabled={loading}>
          {loading ? 'Analyzing…' : 'Analyze'}
        </button>
      </form>

      {error && <p className="text-red-600 mt-4">{error}</p>}

      {result && (
        <div className="mt-5 text-center">
          <h2 className="font-semibold text-lg">{result.vehicle || 'Vehicle'}</h2>
          <p className="text-gray-700">{result.summary}</p>
          <button onClick={downloadReport} className="mt-4 bg-gray-800 text-white px-4 py-2 rounded">
            Download Report (PDF)
          </button>
        </div>
      )}
    </div>
  );
}
