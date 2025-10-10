import React, { useState, useEffect } from 'react';
import { getDrugAlternatives } from '../services/drugAlternativesService';

const DrugAlternatives = ({ rxcui }) => {
  const [alternatives, setAlternatives] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAlternatives = async () => {
      try {
        const data = await getDrugAlternatives(rxcui);
        setAlternatives(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchAlternatives();
  }, [rxcui]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Drug Alternatives</h2>
      {alternatives.length > 0 ? (
        <ul>
          {alternatives.map((alt) => (
            <li key={alt.rxcui}>
              <strong>{alt.name}</strong> ({alt.category}) - Tier {alt.tier} - Est. Annual Cost: ${alt.estimated_annual_cost}
            </li>
          ))}
        </ul>
      ) : (
        <p>No alternatives found.</p>
      )}
    </div>
  );
};

export default DrugAlternatives;
