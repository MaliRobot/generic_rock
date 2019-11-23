# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:27:25 2017

@author: Misha
"""

from bs4 import BeautifulSoup, NavigableString
import urllib.request
import json, codecs

BASE_URL = 'http://www.svastara.com/muzika/?slovo='
ARTIST_KEYS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#'


def get_artists():
    links = {}

    for i in range(len(ARTIST_KEYS)):
        if ARTIST_KEYS[i] == '#':
            url = BASE_URL + '0-9'
        else:
            url = BASE_URL + ARTIST_KEYS[i]

        with urllib.request.urlopen(url) as response:
            print('Fetching letter ' + ARTIST_KEYS[i] + ' from url: ' + url)
            html = response.read()
            soup = BeautifulSoup(html, "lxml")
            artists = soup.find_all("tr", { "class" : "list" })
            if artists:
                for artist in artists:
                    links[artist.find_all('a')[0].get_text()] = artist.find_all('a')[0]['href']

        print(links)

    with codecs.open('artist_links.json', 'w', "utf-8") as fp:
        json.dump(links, fp, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    get_artists()