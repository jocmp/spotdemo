import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, request, render_template

app = Flask(__name__)


def track_item(result):
    (idx, track) = result
    return {"index": idx + 1, "track_name": track['name']}


def fetch_music(query):
    if not query:
        return []

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    results = sp.search(q=query, limit=20)
    return list(map(track_item, enumerate(results['tracks']['items'])))


@app.route('/')
def index():
    query = request.args.get('q', '')
    results = fetch_music(query=query)

    return render_template('index.html', results=results, query=query)
