import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, request, render_template

app = Flask(__name__)


def fetch_music(query):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    results = sp.search(q=query, limit=20)
    serialized = []
    for idx, track in enumerate(results['tracks']['items']):
        serialized.append({"index": idx + 1, "track_name": track['name']})
    
    return serialized


@app.route('/')
def index():
    query = request.args.get('q', '')
    results = fetch_music(query=query)
    return render_template('index.html', results=results)
