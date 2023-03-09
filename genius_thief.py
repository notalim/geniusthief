# Make HTTP requests
import requests
# Scrape data from an HTML document
from bs4 import BeautifulSoup
# I/O
import os
# Search and manipulate strings
import re

GENIUS_API_TOKEN='insert token here'

# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response
# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
    page = 1
    songs = []
    
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)
    
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
            
        if (len(songs) == song_cap):
            break
        else:
            page += 1
        
    print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs
    
def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics_container = html.find('div', class_ = "Lyrics__Container-sc-1ynbvzw-6 YYrds")
    # ADD a "\n" before every <br/>
    for br in lyrics_container.find_all("br"):
        br.replace_with("\n")
    lyrics_lines = lyrics_container.get_text().split("\n")
    #remove identifiers like chorus, verse, etc
    lyrics_lines = [re.sub(r'[\(\[].*?[\)\]]', '', line) for line in lyrics_lines]
    #remove empty lines
    lyrics_lines = [(line.strip()) for line in lyrics_lines if line.strip()]

    lyrics = os.linesep.join(lyrics_lines)
    return lyrics

# DEMO
#print(scrape_song_lyrics('inser a song lyric'))

def write_lyrics_to_file(artist_name, song_count):
    f = open('lyrics/' + artist_name.lower() + '.txt', 'w', encoding="utf-8")
    urls = request_song_url(artist_name, song_count)
    for url in urls:
        lyrics = scrape_song_lyrics(url)
        f.write(lyrics)
        f.write('\n\n') # Add a newline character after each song's lyrics
    f.close()
    num_lines = sum(1 for line in open('lyrics/' + artist_name.lower() + '.txt', 'rb'))
    print('Wrote {} lines to file from {} songs'.format(num_lines, song_count))
  
# DEMO  
write_lyrics_to_file('insert artist name here', 100)

