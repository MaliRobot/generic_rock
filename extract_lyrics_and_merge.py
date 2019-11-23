
import json, os
from bs4 import BeautifulSoup

PATH = 'out/artists'

def extract_lyrics():
    titles = []
    lyrics = []

    files = os.listdir(PATH)
    for f in files:
        with open(PATH + '/' + f, "r") as read_file:
            data = json.load(read_file)
        key = next(iter(data))
        for song in data[key]:
            soup = BeautifulSoup(song['lyrics'], features='lxml')
            text_list = soup.getText(separator=u' ').split('\n')
            title = text_list[2].strip().split('-')[1]
            lyric = text_list[3]
            titles.append(str(title))
            lyrics.append(str(lyric))

    titles_file = open('out/all_titles_processed.txt', 'w', encoding="utf-8")
    titles_file.write(' '.join(titles))

    lyrics_file = open('out/all_lyrics_processed.txt', 'w', encoding="utf-8")
    lyrics_file.write(' '.join(lyrics))


if __name__ == '__main__':
    extract_lyrics()