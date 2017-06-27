#!/usr/bin/python
#coding=utf-8

import os
import json
from Song import Song

def load():
    with open("data_1") as json_file:
        data = json.load(json_file)

        array = []
        for son in data["data"]["data"]["songs"]:
            aname = son["singers"]
            song_name = son["songName"]

            listenFiles = son["listenFiles"]
            maxSize = 0
            fm = ""
            for files in listenFiles:
                size = float(files["fileSize"]) / 1024 / 1024
                if maxSize < size:
                    maxSize = size
                    lfile = files["listenFile"]
                    fm = files["format"]

            print  aname
            print song_name
            print lfile
            print maxSize

            newSong = Song(artist_name = aname,song_name = song_name, url = lfile,size=maxSize,format=fm)
            array.append(newSong)
        for ns in array:
            ns.startDown()

if __name__ == '__main__':
    load()
