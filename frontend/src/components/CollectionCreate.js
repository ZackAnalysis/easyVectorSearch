import React, { useState } from 'react';
import axios from 'axios';

const CollectionCreate = () => {
  const [file, setFile] = useState(null);
  const [collectionName, setCollectionName] = useState('');
  const [textField, setTextField] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleCollectionNameChange = (e) => {
    setCollectionName(e.target.value);
  };

  const handleTextFieldChange = (e) => {
    setTextField(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    formData.append('collectionName', collectionName);
    formData.append('textField', textField);

    try {
      const response = await axios.post('/api/collections', formData);
      if (response.status === 200) {
        alert('Collection created successfully');
      }
    } catch (error) {
      alert('Failed to create collection');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        JSON File:
        <input type="file" onChange={handleFileChange} />
      </label>
      <label>
        Collection Name:
        <input type="text" value={collectionName} onChange={handleCollectionNameChange} />
      </label>
      <label>
        Text Field:
        <input type="text" value={textField} onChange={handleTextFieldChange} />
      </label>
      <button type="submit">Create Collection</button>
    </form>
  );
};

export default CollectionCreate;