import pytest
from app import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Setup a test config
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SECRET_KEY": "test_secret_key", # a fake secret key for tests
        "WTF_CSRF_ENABLED": False # Disable CSRF for form testing
    })
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_index_get(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Spotify Playlist Exporter" in response.data

def test_post_valid_playlist(client, mocker):
    """Test exporting a valid playlist URL."""
    # Mock the spotipy client
    mock_sp = mocker.patch('app.sp')

    # Mock the playlist data
    mock_sp.playlist.return_value = {
        'name': 'Test Playlist',
        'tracks': {
            'items': [
                {'track': {'name': 'Song 1', 'artists': [{'name': 'Artist A'}], 'album': {'name': 'Album X'}, 'duration_ms': 180000}},
                {'track': {'name': 'Song 2', 'artists': [{'name': 'Artist B'}], 'album': {'name': 'Album Y'}, 'duration_ms': 240000}},
            ],
            'next': None
        }
    }

    response = client.post('/', data={'playlist_url': 'https://open.spotify.com/playlist/valid_id'})

    assert response.status_code == 200
    assert response.mimetype == 'text/csv'
    assert response.headers['Content-Disposition'] == 'attachment; filename=Test_Playlist.csv'

    csv_data = response.data.decode('utf-8')
    assert "Song 1,Artist A,Album X,180000" in csv_data
    assert "Song 2,Artist B,Album Y,240000" in csv_data

def test_post_invalid_playlist_url(client):
    """Test submitting an invalid Spotify URL."""
    response = client.post('/', data={'playlist_url': 'https://not-spotify.com/playlist/invalid'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid Spotify playlist URL.' in response.data

def test_post_spotify_api_error(client, mocker):
    """Test handling of Spotify API errors."""
    mock_sp = mocker.patch('app.sp')
    from spotipy.exceptions import SpotifyException
    mock_sp.playlist.side_effect = SpotifyException(404, -1, "Not found")

    response = client.post('/', data={'playlist_url': 'https://open.spotify.com/playlist/not_found_id'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'An error occurred with the Spotify API.' in response.data
