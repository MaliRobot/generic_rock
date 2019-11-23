# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:05:56 2017

@author: Misha
"""

from bs4 import BeautifulSoup
import urllib.request
import json, codecs

BASE_URL = 'http://www.svastara.com/muzika/'

songs_dict = {}
    
data = json.loads(open('artist_links.json', 'r', encoding='utf-8').read())


def get_song_links(data):
    todo = set(data.keys())
    
    while len(todo) > 0:
        for artist in data:
            if artist not in todo:
                continue
            url = BASE_URL + data[artist]
            try:
                with urllib.request.urlopen(url) as response:
                    html = response.read()
                    soup = BeautifulSoup(html, "lxml")
                    songs = soup.find_all("tr", { "class" : "list" })
                    for song in songs:
                        song_data = song.td.a
                        if artist in songs_dict:
                            songs_dict[artist].append({'url':song_data['href'],'title':song_data.text})
                        else:
                            songs_dict[artist] = [{'url':song_data['href'],'title':song_data.text}]
                    todo.remove(artist)
            except Exception as e:
                print(e)
                print(artist)
 
    with codecs.open('songs_links.json', 'w', "utf-8") as fp:
        json.dump(songs_dict, fp, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    get_song_links(data)
