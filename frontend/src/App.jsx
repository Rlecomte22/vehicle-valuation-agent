import React from 'react';
import ValuationForm from './components/ValuationForm';
import './index.css';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <h1 className="text-3xl font-bold mb-6">AI Vehicle Valuation Agent</h1>
      <ValuationForm />
    </div>
  );
}
