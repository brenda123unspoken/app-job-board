import React, { useState } from 'react';
import axios from 'axios';

const PostJob = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [message, setMessage] = useState('');

  const handlePostJob = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token'); // JWT from login
      const response = await axios.post(
        'http://127.0.0.1:5000/jobs',
        { title, description },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setMessage('Job posted successfully!');
    } catch (error) {
      setMessage('Failed to post job.');
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Post a New Job</h2>
      <form onSubmit={handlePostJob}>
        <div>
          <label>Job Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label>Job Description:</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <button type="submit">Post Job</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default PostJob;
