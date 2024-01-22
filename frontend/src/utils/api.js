import axios from 'axios';

const API_URL = 'http://localhost:8000'; // replace with your API's URL

export const getCollectionList = async () => {
  const response = await axios.get(`${API_URL}/collections`);
  return response.data;
};

export const createCollection = async (collectionData) => {
  const response = await axios.post(`${API_URL}/collections`, collectionData);
  return response.data;
};

export const deleteCollection = async (collectionId) => {
  const response = await axios.delete(`${API_URL}/collections/${collectionId}`);
  return response.data;
};

export const searchCollection = async (collectionId, searchText, numCandidates) => {
  const response = await axios.get(`${API_URL}/collections/${collectionId}/search`, {
    params: { text: searchText, num_candidates: numCandidates }
  });
  return response.data;
};