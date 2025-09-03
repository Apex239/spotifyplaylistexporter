# Spotify Playlist Exporter

A professional, easy-to-use web application for exporting your Spotify playlists to CSV files. Built with Python and Flask, this tool provides a clean interface to convert playlist data into a spreadsheet-friendly format, complete with track name, artist, album, and duration.

## Key Features

-   **Simple Web Interface:** Just paste a Spotify playlist URL and click "Export". No complex setup required for day-to-day use.
-   **Dynamic CSV Filenames:** Exports files with the playlist's name (e.g., `My_Awesome_Playlist.csv`) for easy organization.
-   **Comprehensive Data:** The CSV includes Track Name, Artist, Album, and Duration (in milliseconds).
-   **Handles Large Playlists:** Automatically paginates through the Spotify API to retrieve all tracks from any size playlist.
-   **Modern UI:** A clean, responsive interface built with Bootstrap 5 that includes a dark mode toggle.
-   **Robust and Tested:** The backend is well-tested to ensure reliability and maintainability.

## Getting Started in 3 Steps

This project includes automated setup scripts to make getting started as simple as possible.

### 1. Clone the Repository

First, clone the repository to your local machine:
```bash
git clone https://github.com/Apex239/spotifyplaylistexporter
cd spotifyplaylistexporter
```

### 2. Add Your Spotify Credentials

You need to provide your Spotify API credentials. The startup script will guide you through this by creating a `.env` file for you from the `.env.example` template.

Open the newly created `.env` file and replace the placeholder values with your credentials from the [Spotify Developer Dashboard](https://developer.spotify.com).

```ini
# .env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
...
```
The `FLASK_SECRET_KEY` will be generated and added for you automatically by the script.

### 3. Run the Startup Script

Now, simply run the appropriate script for your operating system. This single command will handle creating a virtual environment, installing dependencies, and starting the application.

## Getting Started

Follow these instructions to set up and run the project on your local machine for development or personal use.

### Prerequisites

-   Python 3.8+
-   A Spotify Developer account to get API credentials. You can create one on the [Spotify Developer Dashboard](https://developer.spotify.com).

### Installation and Configuration

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Apex239/spotifyplaylistexporter
    cd spotifyplaylistexporter
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install the required packages
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a file named `.env` in the project root and add your credentials.
    First, generate a secret key for Flask:
    ```bash
    python -c "import secrets; print(secrets.token_hex(16))"
    ```
    Now, create the `.env` file with the following content, replacing the placeholder values with your actual credentials and the generated secret key:
    ```ini
    # .env
    SPOTIFY_CLIENT_ID=your_spotify_client_id
    SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
    FLASK_SECRET_KEY=your_generated_flask_secret_key
    ```

### Running the Application

Once the configuration is complete, you can start the application using the provided startup scripts:

-   **On macOS/Linux:**
    ```bash
    ./start.sh
    ```
-   **On Windows:**
    ```bash
    ./start.bat
    ```
The script will perform all necessary checks. If your Spotify credentials are correct, the application will start, and you can access it at `http://127.0.0.1:5000`.
The application will be available at `http://127.0.0.1:5000`.

## For Developers

This section provides information for those who wish to contribute to or extend the project.

### Project Structure

The project follows a standard Flask application structure:

```
.
├── .env              # Environment variables (not version controlled)
├── app.py            # Main Flask application, contains routing and app factory
├── helpers.py        # Helper functions for URL parsing and filename sanitization
├── requirements.txt  # Project dependencies
├── start.bat         # Startup script for Windows
├── start.sh          # Startup script for macOS/Linux
├── templates/
│   └── index.html    # Main HTML template for the web interface
└── tests/
    ├── test_app.py   # Integration tests for the Flask app
    └── test_helpers.py # Unit tests for helper functions
```

### Running Tests

This project uses `pytest` for testing. To run the full test suite, execute the following command from the root directory:

```bash
pytest
```

The tests include unit tests for the helper functions and integration tests that mock the Spotify API, ensuring that the application logic is correct without making real network calls.

## Contributing

Contributions are welcome! If you have a suggestion or find a bug, please open an issue to discuss it.

If you wish to contribute code, please follow these steps:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Ensure all tests pass (`pytest`).
5.  Commit your changes (`git commit -m 'Add some feature'`).
6.  Push to the branch (`git push origin feature/YourFeature`).
7.  Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
