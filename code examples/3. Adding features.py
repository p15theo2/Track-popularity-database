#!/usr/bin/env python
# coding: utf-8
import pandas as mp,csv,spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials('0ac98a8f556a46f48024c6cde776c1b0','fbf695854344424e9539c05bbae31ad3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
dtf = mp.read_csv('tracksandspotifyids-cleaned.csv')
with open('spotifyfeatures.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Add the header/column names
    header = ['duration_ms','energy','key', 'mode', 'time_signature' , 'acousticness','danceability','instrumentalness','liveness','loudness','speechiness','valence','tempo']
    writer.writerow(header)
    # Iterate over `data`  and  write to the csv file
    
    for row in dtf["track_id"]:
        try:
            track= sp.audio_features(tracks=[row])
            features = [
            track[0]['duration_ms'],
            track[0]['energy'],
            track[0]['key'],
            track[0]['mode'],
            track[0]['time_signature'],
            track[0]['acousticness'],
            track[0]['danceability'],
            track[0]['instrumentalness'],
            track[0]['liveness'],
            track[0]['loudness'],
            track[0]['speechiness'],
            track[0]['valence'],
            track[0]['tempo']]
            writer.writerow(features)
        except:
            print("no features for"+str(row))
            features = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            writer.writerow(features)
            
features = mp.read_csv('spotifyfeatures.csv')
spotify_trackfeatures = mp.concat([dtf, features], axis=1)
spotify_trackfeatures = spotify_trackfeatures[spotify_trackfeatures["duration_ms"]!=0]
spotify_trackfeatures['On_chart'] = 1
track = sp.audio_features(tracks=['5TWAIHYaOnYg4txfmCgon5'])
print (track[0]['duration_ms'],
       track[0]['key'],
       track[0]['energy'],
       track[0]['mode'],
       track[0]['time_signature'],
       track[0]['acousticness'],
       track[0]['danceability'],
       track[0]['instrumentalness'],
       track[0]['liveness'],
       track[0]['loudness'],
       track[0]['speechiness'],
       track[0]['valence'],
       track[0]['tempo'],)

spotify_trackfeatures.to_csv("famouscomplete.csv",index=False)

