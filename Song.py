#coding=utf-8

import urllib2
import os

class Song:
    count = 0
    finish = 0
    def __init__(self,artist_name,song_name,url,size,format):
        self.artist_name = artist_name
        self.song_name = song_name
        self.url = url
        self.size = size
        self.format = format;
        Song.count += 1

    def startDown(self):
        Song.finish += 1
        print "第"+str(Song.finish)+"个文件开始下载..."

        url = self.url
        localPath = "/Users/panlee/Desktop/music/"+self.artist_name+"/"
        mp3name = self.song_name + "." + self.format

        if not os.path.isdir(localPath):
            os.mkdir(localPath)
        localPath = localPath + mp3name

        if not os.path.exists(localPath):
            f = urllib2.urlopen(url)
            with open(localPath, "wb") as code:
                code.write(f.read())

        print "完成下载第"+str(Song.finish)+"个,共"+str(Song.count)+"个"
        if Song.finish == Song.count:
            print "完成下载所有文件"
