#!/usr/bin/python
import os
import sys
import urllib
from urllib import *


###README
#TODO add description  of script here and to main README.txt




# MetaCritic is a site that posts reviews on movies, tv, games, music, etc.
# This link connects specifically to game reviews for the iPhone/iPad

filename = 'link-list.txt'
links_file = open(filename) # Opens text file that contains list of links
print("working on list of link file: " + filename)

links = links_file.readlines()

cleanLinks = [] # Contains a cleaned list of all links to metacritic
for item in links:
    if item != "\n":
        cleanLinks.append(item.strip())


#Iterates through list of links and prints html source code to file
for link in cleanLinks:
    print("processing: " + link)
    linkList = link.split('/')
    title = linkList[-1]
    print("title: " + title)
         
    webPage = URLopener().open(link)
    htmlDoc = webPage.read()
    webPage.close()
    outFile = open('../data/train/' + title + '.htm', 'w')
    writeToFile = outFile.write(htmlDoc)
    print("wrote to file: " + '../data/train/' + title + '.htm\n')
    

