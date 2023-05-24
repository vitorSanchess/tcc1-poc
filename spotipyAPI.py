import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

playlist_uri = '0eyKYTmDP9GsdBonIouIpg'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='a3df5467c42c40469f90b2bdcb8883c6',
                                                                          client_secret='a34ebbbf6d784a06914c2a43a0293356'))

results = sp.playlist(playlist_uri, fields='tracks')
tracks = results['tracks']['items']
# Create an empty list to store track information
user_playlist = []

# Iterate over the tracks and append track URI and name to user_playlist
for track in tracks:
    track_uri = track['track']['uri']
    track_name = track['track']['name']
    for artist in track['track']['artists']:
        track_artists = artist['name']
    user_playlist.append({
        'uri': track_uri, 
        'name': track_name,
        'artist': track_artists
    })
print(user_playlist)
# Create a playlist with the given track URIs
def create_playlist_with_tracks(track_uris):
    # Get the user's ID
    user = sp.current_user()
    user_id = user['id']

    # Create a new playlist
    playlist = sp.user_playlist_create(user=user_id, name='My Playlist', public=True)

    # Add tracks to the playlist
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

    print('Playlist created successfully!')
