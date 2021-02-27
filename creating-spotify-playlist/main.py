import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()
import os
from pprint import pprint

cid = os.getenv("cid")
secret = os.getenv("secret")
user_id = os.getenv("user_id")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=cid,
        client_secret=secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
# user_id = sp.current_user()["id"]

date = input("What year would you like to travel? (Enter in YYYY-MM-DD format): ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
# print(URL)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all(class_="chart-element__information__song")
songs = [song.getText() for song in songs]
songs_uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:{date.split('-')[0]}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} isn't available on spotify. skipped to next")

# print(songs_uris)
playlist_id = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)["id"]
# print(playlist_id)
sp.playlist_add_items(playlist_id, songs_uris)