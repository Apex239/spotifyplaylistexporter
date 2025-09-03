import re

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


def sanitize_filename(name):
    """Sanitizes a string to be a valid filename."""
    name = name.strip()
    # Remove invalid characters that are common across OSes
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace spaces with underscores for better compatibility
    name = name.replace(' ', '_')
    # Limit length to avoid filesystem errors
    name = name[:150]
    # If the name ends up empty after sanitization, provide a default
    if not name:
        return "playlist.csv"
    return f"{name}.csv"
