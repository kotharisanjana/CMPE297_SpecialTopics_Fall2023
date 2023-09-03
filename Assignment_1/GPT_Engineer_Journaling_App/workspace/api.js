const API_URL = 'http://localhost:5000/entries';

export function getEntries() {
  return fetch(API_URL).then((response) => response.json());
}

export function getEntry(id) {
  return fetch(`${API_URL}/${id}`).then((response) => response.json());
}

export function updateEntry(id, entry) {
  return fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(entry),
  });
}

export function createEntry(entry) {
  return fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(entry),
  });
}
