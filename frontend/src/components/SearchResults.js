import React from 'react';

const SearchResults = ({ results }) => {
  if (!results || results.length === 0) {
    return <p>No results found</p>;
  }

  return (
    <div>
      <h2>Search Results</h2>
      {results.map((result, index) => (
        <div key={index}>
          <p>Content: {result.content}</p>
          <p>Score: {result.score}</p>
        </div>
      ))}
    </div>
  );
};

export default SearchResults;