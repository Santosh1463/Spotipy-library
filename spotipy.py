import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "your-client-id"
client_secret = "your-client-secret"

artist_name = "The Beatles"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q=artist_name, type="artist")
artist_id = results["artists"]["items"][0]["id"]

top_tracks = sp.artist_top_tracks(artist_id)

most_streamed_song = None
most_streams = 0

for track in top_tracks["tracks"]:
    streams = track["popularity"]

    if streams > most_streams:
        most_streamed_song = track["name"]
        most_streams = streams

print(f"The song with the most streams by {artist_name} is '{most_streamed_song}' with {most_streams} streams.")