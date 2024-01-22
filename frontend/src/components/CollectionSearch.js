import React, { useState } from 'react';
import axios from 'axios';

const CollectionSearch = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [results, setResults] = useState([]);
  const [numResults, setNumResults] = useState(10);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`/api/search?term=${searchTerm}&numResults=${numResults}`);
      setResults(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={e => setSearchTerm(e.target.value)}
        placeholder="Search..."
      />
      <input
        type="number"
        value={numResults}
        onChange={e => setNumResults(e.target.value)}
        placeholder="Number of results..."
      />
      <button onClick={handleSearch}>Search</button>
      {results.map((result, index) => (
        <div key={index}>
          <p>{result.content}</p>
          <p>Score: {result.score}</p>
        </div>
      ))}
    </div>
  );
};

export default CollectionSearch;