import React, { useState, useEffect } from 'react';
import { getEntry, updateEntry, createEntry } from './api';

function JournalEntryForm({ match }) {
  const [entry, setEntry] = useState({ title: '', content: '' });

  useEffect(() => {
    if (match.params.id) {
      getEntry(match.params.id).then((entry) => setEntry(entry));
    }
  }, [match.params.id]);

  const handleChange = (event) => {
    setEntry({ ...entry, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (match.params.id) {
      updateEntry(match.params.id, entry);
    } else {
      createEntry(entry);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Title:
        <input type="text" name="title" value={entry.title} onChange={handleChange} />
      </label>
      <label>
        Content:
        <textarea name="content" value={entry.content} onChange={handleChange} />
      </label>
      <button type="submit">Save</button>
    </form>
  );
}

export default JournalEntryForm;
