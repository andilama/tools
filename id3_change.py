# -*- coding: cp1252 -*-
import eyed3
import eyed3.id3
import re
import glob
import os
import shutil


mp3_path = "C:\Users\Julia\Music\iTunes Music\Sj�wall_Wahl��\Mannen som gick upp i r�k"
os.chdir(mp3_path)
files = os.listdir(os.curdir)

for mp3file in files:
    if mp3file.endswith('06 006-Mannen som gick upp i r�k.mp3'):
        audiofile = eyed3.load(mp3file, (2,None,None))
        print audiofile.tag.album
        
        #old_title = audiofile.tag.title
        #new_title = old_title.replace('_','-')
        #print new_title
        #audiofile.tag.title = new_title
        #audiofile.tag.artist = u'Sj�wall/Wahl��'
        audiofile.tag.album = u'Mannen som gick upp i r�k'
        audiofile.tag.save()
        print audiofile.tag.artist
