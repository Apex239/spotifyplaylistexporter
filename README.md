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

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Apex239/spotifyplaylistexporter
   cd spotifyplaylistexporter
