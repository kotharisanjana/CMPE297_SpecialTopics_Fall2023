# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the Python dependencies
pip install -r requirements.txt

# Run the Flask application
FLASK_APP=app.py flask run

# Install the Node.js dependencies
npm install

# Run the React application
npm start
