# Spotify Playlist to CSV Exporter

A web application that exports Spotify playlists into CSV (spreadsheet) files. Built with Python, Flask, and Spotipy, this project provides a user-friendly web interface that allows you to quickly convert your favorite Spotify playlists into CSV format.

## Features

- **Export Playlists:** Enter a Spotify playlist URL to download a CSV file containing track details (Name, Artist, Album, Duration in milliseconds).
- **Responsive Web Interface:** Enjoy a modern, professional UI built with Bootstrap 5.
- **Cross-Platform Support:** Startup scripts for Unix-like systems (`start.sh`) and Windows (`start.bat`) ensure easy setup on any platform.
- **Efficient Pagination Handling:** Automatically retrieves all tracks even for large playlists.
- **Robust Error Handling:** Provides clear flash messages for invalid inputs or processing errors.

## Prerequisites

- **Python:** Version 3.6 or later.
- **Spotify Developer Account:** Register an application on the [Spotify Developer Dashboard](https://developer.spotify.com) to obtain your `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`.
- **Operating System:**  
  - Unix-like systems: Use a Bash terminal to run `start.sh`.  
  - Windows: Use Command Prompt, PowerShell, or Git Bash to run `start.bat`.

## Installation

**Clone the Repository:**
```bash
git clone https://github.com/Apex239/spotifyplaylistexporter
cd spotifyplaylistexporter
```

### Generating a Flask Secret Key

The `FLASK_SECRET_KEY` is required to sign session cookies and other security-related tokens in Flask. You must generate a strong random key before running the app. To do this, run the following command:

```bash
python -c "import secrets; print(secrets.token_hex(16))"
```

### Configuration

Before running the application, you need to set up your environment variables.

```ini
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
FLASK_SECRET_KEY=your_flask_secret_key
```

## Running the Application

To start the Flask app, use the appropriate startup script:

For Unix-like systems:
```bash
./start.sh
```

For Windows:
```bash
./start.bat
```

Once running, open `http://127.0.0.1:5000` in your browser to access the application.

## License

This project is licensed under the MIT License.
