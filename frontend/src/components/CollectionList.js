import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const CollectionList = () => {
  const [collections, setCollections] = useState([]);

  useEffect(() => {
    fetchCollections();
  }, []);

  const fetchCollections = async () => {
    const res = await axios.get('/api/collections');
    setCollections(res.data);
  };

  const deleteCollection = async (collection) => {
    await axios.delete(`/api/collections/${collection}`);
    fetchCollections();
  };

  return (
    <div>
      <h1>Collections</h1>
      {collections.map((collection) => (
        <div key={collection}>
          <Link to={`/collections/${collection}`}>{collection}</Link>
          <button onClick={() => deleteCollection(collection)}>Delete</button>
        </div>
      ))}
      <Link to="/collections/new">Create New Collection</Link>
    </div>
  );
};

export default CollectionList;