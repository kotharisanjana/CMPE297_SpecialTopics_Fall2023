import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import JournalEntryList from './JournalEntryList';
import JournalEntryForm from './JournalEntryForm';

function App() {
  return (
    <Router>
      <div>
        <Route exact path="/" component={JournalEntryList} />
        <Route path="/entry/:id" component={JournalEntryForm} />
      </div>
    </Router>
  );
}

export default App;
