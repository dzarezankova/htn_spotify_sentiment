from flask import Flask, redirect, render_template
from app import app
import urllib
from urllib.parse import quote

# Import spotify cilent IDs and secrets

CLIENT_ID = "2f3c4641f2b04770842408e01d627b74"
CLIENT_SECRET = "dc1797eeaa5045f3814ddd362d529c9c"

spotify_auth_url = "https://accounts.spotify.com/authorize"
spotify_token_url = "https://accounts.spotify.com/api/token"
spotify_api_base_url = "https://api.spotify.com"

# Import urls for our app 

client_side_url = "http://127.0.0.1:5000/"
redirect_uri = "http://127.0.0.1:5000/spotify_sentiment_analysis"
scope = 'user-read-private user-read-playback-state user-modify-playback-state user-library-read'
state = ""
show_dialogue_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "client_id": CLIENT_ID
}

@app.route('/spotify_sentiment_analysis_login')
def spotify():
    return render_template('spotify_sentiment_analysis_login.html')

@app.route('/spotify_authentication')
def spotify_auth():
    url_args = "&".join(["{}={}".format(key,urllib.parse.quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)
 
@app.route('/spotify_sentiment_analysis')
def spotify_sentiment_analysis():
    return render_template('spotify_sentiment_analysis.html')

@app.route('/spotify_sentiment_analysis_test')
def index():
    return "Hello, World!"
    user = 'Listener'
    return render_template('index.html', user=user)
