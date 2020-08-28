import streamlit as st
import pickle
import numpy as np
import pandas as pd
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_prediction():
    audio_features = sp.audio_features(results['tracks']['items'][0]['id'])
    X = pd.json_normalize(audio_features[0])
    X_clean = X.drop(['type', 'id', 'uri', 'track_href', 'analysis_url'], axis=1)
    if (model.predict(X_clean)[0])==0:
        st.write('If released today, it would **NOT** be **HOT** :cry: Probability', int((model.predict_proba(X_clean)[0][0])*100), '%')
    else:
        st.balloons()
        st.write('If released today, it would be **HOT!!!** :smile: Probability', int((model.predict_proba(X_clean)[0][1])*100), '%')
    track = sp.track(X['id'][0])
    st.write('Artist: ', pd.json_normalize(track)['artists'][0][0]['name'])
    st.write('Song:   ', pd.json_normalize(track)['name'][0])
    st.write('Album:  ', pd.json_normalize(track)['album.name'][0])
    st.write('Year:   ', pd.json_normalize(track)['album.release_date'][0][0:4])
    preview = pd.json_normalize(track)['preview_url'][0]
    if preview is not None:
        st.audio(preview)
    st.image(pd.json_normalize(track)['album.images'][0][0]['url'], use_column_width=True, width=None)

st.image('hnp_logo.jpeg', use_column_width=True, width=None, output_format='JPEG')

with open('settings.env') as f:
    env_vars = json.loads(f.read())
os.environ['SPOTIPY_CLIENT_ID'] = env_vars['SPOTIPY_CLIENT_ID']
os.environ['SPOTIPY_CLIENT_SECRET'] = env_vars['SPOTIPY_CLIENT_SECRET']

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

model = pickle.load(open("model.pkl","rb"))

query = st.text_input('Please enter song name or artist + song name', value='')

if query != '':
    results = sp.search(q = query, type='track', market='US')

    if not results["tracks"]["items"]:
        st.warning('No results found. Please try again')
    else:
        get_prediction()
