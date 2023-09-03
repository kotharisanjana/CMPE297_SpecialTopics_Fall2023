import React, { useEffect, useState } from 'react';
import { getEntries } from './api';

function JournalEntryList() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    getEntries().then((entries) => setEntries(entries));
  }, []);

  return (
    <div>
      {entries.map((entry) => (
        <div key={entry.id}>
          <h2>{entry.title}</h2>
          <p>{entry.content}</p>
        </div>
      ))}
    </div>
  );
}

export default JournalEntryList;
