from flask import Flask, request, jsonify
from db import db_init, db
from models import JournalEntry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route('/entries', methods=['GET', 'POST'])
def handle_entries():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_entry = JournalEntry(title=data['title'], content=data['content'])
            db.session.add(new_entry)
            db.session.commit()
            return {"message": f"entry {new_entry.title} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        entries = JournalEntry.query.all()
        results = [
            {
                "title": entry.title,
                "content": entry.content,
                "date": entry.date
            } for entry in entries]

        return {"count": len(results), "entries": results, "message": "success"}

@app.route('/entries/<entry_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)

    if request.method == 'GET':
        response = {
            "title": entry.title,
            "content": entry.content,
            "date": entry.date
        }
        return {"message": "success", "entry": response}

    elif request.method == 'PUT':
        data = request.get_json()
        entry.title = data['title']
        entry.content = data['content']
        db.session.add(entry)
        db.session.commit()
        return {"message": f"entry {entry.title} has been updated successfully."}

    elif request.method == 'DELETE':
        db.session.delete(entry)
        db.session.commit()
        return {"message": f"entry {entry.title} has been deleted successfully."}

if __name__ == '__main__':
    app.run(debug=True)
