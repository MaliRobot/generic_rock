# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:47:16 2017

@author: Milosh
"""

from bs4 import BeautifulSoup
import urllib.request
import json, codecs, os.path

BASE_URL = 'http://www.svastara.com/muzika/'
    
done_list = 'artists.txt'
data = json.loads(open('songs_links.json', 'r', encoding='utf-8').read())

def get_songs(data):
    if os.path.exists(done_list):
        artists = open(done_list, 'r').read()
        artists = set([x.strip() for x in artists.split('\n')])
    else:
        artists = set()
        _ = open(done_list, 'w').close()
    for artist in data:
        artist_check = safe_str(artist)
        if artist_check in artists:
            continue
        songs = {artist:[]}
        print('Fetching songs by ' + artist)
        for song in data[artist]:
            url = BASE_URL + song['url']
            success = False
            while success == False:
                try:
                    with urllib.request.urlopen(url) as response:
                        html = response.read()
                        soup = BeautifulSoup(html, "lxml")
                        lyrics = soup.find_all("div", { "id" : "content-right" })
                        song.update({'lyrics':str(lyrics)})
                        songs[artist].append(song)
                        success = True
                except Exception as e:
                    print(e)
        filename = safe_str(artist)
        with codecs.open('out/artists/%s.json' % (filename), 'w', "utf-8") as fp:
            json.dump(songs, fp, indent=4, separators=(',', ': '))
        with open(done_list, 'a+') as fp:
            fp.write(filename +'\n')

def safe_str(string):
    string = "".join([c for c in string if c.isalpha() or c.isdigit() or c==' ' and c not in '*."/\[]:;|=,']).rstrip()
    string = string.replace('ć','c')
    string = string.replace('Ć','C')
    string = string.replace('č','c')
    string = string.replace('Č','C')
    string = string.replace('Đ','dj')
    string = string.replace('đ','dj')
    return string
    
get_songs(data)
