from flask import Flask, redirect, render_template, make_response
from app import app
import urllib
from urllib.parse import urlencode
import json
import base64
import requests
from flask import request, session
import spotipy
import random as rand
import string as string
from musixmatch import Musixmatch
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Import spotify client IDs and secrets
CLIENT_ID = "2f3c4641f2b04770842408e01d627b74"
CLIENT_SECRET = "dc1797eeaa5045f3814ddd362d529c9c"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1:5000/"
REDIRECT_URI = "http://127.0.0.1:5000/callback"
SCOPE = 'user-read-private user-read-playback-state user-modify-playback-state user-library-read playlist-read-private'
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

# Listener information
user_id = ''
username = ''
profile_url = ''
profile_data = {}


auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "client_id": CLIENT_ID
}


@app.route('/authorize')
def authorize():
    client_id = CLIENT_ID
    redirect_uri = REDIRECT_URI
    scope = SCOPE

    authorize_url = 'https://accounts.spotify.com/en/authorize?'
    params = {'response_type': 'code', 'client_id': client_id,
              'redirect_uri': redirect_uri, 'scope': scope,
              }
    query_params = urlencode(params)
    response = make_response(redirect(authorize_url + query_params))
    return response


@app.route('/callback')
def callback():
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }

    base64encoded = base64.b64encode(
        "{}:{}".format(CLIENT_ID, CLIENT_SECRET).encode())
    headers = {"Authorization": "Basic {}".format(base64encoded.decode())}
    post_request = requests.post(
        SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    # Get profile data
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(
        user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)

    print(profile_data)
    user_id = profile_data['id']
    username = profile_data['display_name']
    profile_url = profile_data['external_urls']['spotify']
    return profile_data


def get_playlist():
    playlist_api_endpoint = "{}/tracks".format(user_profile_api_endpoint)
    playlists_response = requests.get(
        playlist_api_endpoint, headers=authorization_header)

    playlist_data = playlists_response.text
    playlist_data = playlist_data[83:-142]
    playlist_data = json.loads(playlist_data)

    playlist_list = []

    for i in playlist_data:
    tmp = [i['added_at'][:-10],
           i['track']['name'],
           i['track']['artists'][0]['name'],
           i['track']['album']['images'][0]['url'],
           i['track']['external_urls']['spotify'],
           i['track']['id']]
    playlist_list.append(tmp)

    playlist_df = pd.DataFrame(playlist_list, columns=[
                               'Date', 'Track_Name', 'Artist', 'Cover_Image', 'URL', 'Track_ID'])
    return playlist_df


musixmatch = Musixmatch('1d6fc3a84d79ec44e7a0d41542f9682e')

analyser = SentimentIntensityAnalyzer()

sentiment_list = []
sentiment_score_list = []


@app.route('/analysis_generation')
def analysis_generation():
    playlist_df = get_playlist()
    for i in playlist_df[['Track_Name', 'Artist']].values:
        try:
            song = musixmatch.matcher_lyrics_get(i[1], i[0])
            song = song['message']['body']['lyrics']['lyrics_body']
            sentiment_score = analyser.polarity_scores(song)

            if sentiment_score['compound'] >= 0.05:
                sentiment_percentage = sentiment_score['compound']
                sentiment = 'Positive'
            elif sentiment_score['compound'] > -0.05 and sentiment_score['compound'] < 0.05:
                sentiment_percentage = sentiment_score['compound']
                sentiment = 'Neutral'
            elif sentiment_score['compound'] <= -0.05:
                sentiment_percentage = sentiment_score['compound']
                sentiment = 'Negative'

            sentiment_list.append(sentiment)
            sentiment_score_list.append((abs(sentiment_percentage) * 100))

        except:
            sentiment_list.append('None')
            sentiment_score_list.append(0)

    playlist_df['Sentiment'] = sentiment_list
    playlist_df['Sentiment_Score'] = sentiment_score_list
