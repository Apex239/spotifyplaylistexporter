import os
import csv
import io
import re
import logging
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables from .env/.flaskenv if available.
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Create and configure the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Spotify API configuration: ensure these environment variables are set
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
    logger.error("Spotify API credentials not set in environment variables.")
    raise Exception("Spotify API credentials are missing. Set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.")

# Initialize Spotipy with client credentials
spotify_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=spotify_credentials_manager)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playlist_url = request.form.get('playlist_url')
        if not playlist_url:
            flash("Please enter a Spotify playlist URL.", "danger")
            return redirect(url_for('index'))
        # Extract the playlist ID from the URL
        playlist_id = extract_playlist_id(playlist_url)
        if not playlist_id:
            flash("Invalid Spotify playlist URL.", "danger")
            return redirect(url_for('index'))
        try:
            # Retrieve the playlist data from Spotify
            playlist = sp.playlist(playlist_id)
            tracks = playlist.get('tracks')
            track_data = []
            # Spotify paginates the track list; loop through pages if necessary
            while tracks:
                for item in tracks.get('items', []):
                    track = item.get('track')
                    if track:
                        track_data.append({
                            'Name': track.get('name'),
                            'Artist': ', '.join(artist['name'] for artist in track.get('artists', [])),
                            'Album': track.get('album', {}).get('name'),
                            'Duration (ms)': track.get('duration_ms')
                        })
                if tracks.get('next'):
                    tracks = sp.next(tracks)
                else:
                    break
            # Create a CSV file in memory
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=['Name', 'Artist', 'Album', 'Duration (ms)'])
            writer.writeheader()
            for row in track_data:
                writer.writerow(row)
            output.seek(0)
            # Send the CSV file as a download
            return send_file(
                io.BytesIO(output.getvalue().encode('utf-8')),
                mimetype='text/csv',
                as_attachment=True,
                attachment_filename='playlist.csv'
            )
        except Exception as e:
            logger.exception("Error processing playlist: %s", e)
            flash("An error occurred while processing the playlist.", "danger")
            return redirect(url_for('index'))
    return render_template('index.html')

def extract_playlist_id(url):
    """
    Extracts the Spotify playlist ID from the URL.
    Supports URLs like:
    - https://open.spotify.com/playlist/{playlist_id}
    - spotify:playlist:{playlist_id}
    """
    patterns = [
        r'open\.spotify\.com/playlist/([a-zA-Z0-9]+)',
        r'spotify:playlist:([a-zA-Z0-9]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

if __name__ == '__main__':
    # Print message to terminal
    print("Server started. Go to http://localhost:5000/ in your browser.")

    # Start the server using waitress
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
