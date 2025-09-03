import os
import csv
import io
import re
import logging
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException

from helpers import extract_playlist_id, sanitize_filename

# This will be initialized in create_app
sp = None
logger = logging.getLogger(__name__)

def generate_csv(track_data):
    """
    Generates a CSV file (in-memory) from the track data and returns a BytesIO object.
    """
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['Name', 'Artist', 'Album', 'Duration (ms)'])
    writer.writeheader()
    for row in track_data:
        writer.writerow(row)
    output.seek(0)
    return io.BytesIO(output.getvalue().encode('utf-8'))

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    app.secret_key = os.environ.get('FLASK_SECRET_KEY')
    if not app.secret_key and app.env == "production":
        raise Exception("Production error: FLASK_SECRET_KEY environment variable is required.")

    logging.basicConfig(level=logging.INFO)

    global sp
    spotify_credentials_manager = SpotifyClientCredentials(
        client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET')
    )
    sp = spotipy.Spotify(client_credentials_manager=spotify_credentials_manager)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            playlist_url = request.form.get('playlist_url')
            if not playlist_url:
                flash("Please enter a Spotify playlist URL.", "danger")
                return redirect(url_for('index'))

            playlist_id = extract_playlist_id(playlist_url)
            if not playlist_id:
                flash("Invalid Spotify playlist URL.", "danger")
                return redirect(url_for('index'))

            try:
                playlist = sp.playlist(playlist_id)
                tracks = playlist.get('tracks', {})
                track_data = []
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

                playlist_name = playlist.get('name', 'playlist')
                download_filename = sanitize_filename(playlist_name)
                csv_file = generate_csv(track_data)

                return send_file(
                    csv_file,
                    mimetype='text/csv',
                    as_attachment=True,
                    download_name=download_filename
                )
            except SpotifyException as se:
                logger.error("Spotify API error: %s", se)
                flash("An error occurred with the Spotify API. The playlist might be private or invalid.", "danger")
                return redirect(url_for('index'))
            except Exception as e:
                logger.error("Error processing playlist: %s", e)
                flash("An unexpected error occurred.", "danger")
                return redirect(url_for('index'))

        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    print("Server started. Go to http://localhost:5000/ in your browser.")
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
