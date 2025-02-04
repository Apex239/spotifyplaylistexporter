#!/bin/bash
# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask app in the background
python app.py &

# Wait a few seconds to allow the server to start
sleep 2

# Open the default web browser to the app URL
if command -v xdg-open >/dev/null; then
    xdg-open http://localhost:5000/
elif command -v open >/dev/null; then
    open http://localhost:5000/
else
    echo "Please open http://localhost:5000/ in your browser."
fi

# Print a message in the terminal
echo "Server started. Go to http://localhost:5000/ in your browser."

# Wait for background processes to finish
wait
