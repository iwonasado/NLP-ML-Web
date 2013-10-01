#!/usr/bin/python
import os
import sys
import urllib
from urllib import *
import bs4
from bs4 import BeautifulSoup
import random

###README
#TODO add to main readme

# This script takes one argument, the argument should be a web link
directory= sys.argv[1]
fileName= directory.split('/')[-1]
print fileName
metacritic = "http://www.metacritic.com"

def crawl(webPage):
    print("processing: " + webPage + '\n')

    # Opens link and reads source code
    openPage = URLopener().open(webPage) 
    htmlDoc = openPage.read()
    openPage.close()

    # print htmlDoc

    # Creates a beautifulSoup object
    soup = BeautifulSoup(htmlDoc)

    # Finds all links on webpage
    linkList = []
    for link in soup.find_all('a'):
        linkList.append(link.get('href'))

    # Finds valid links (only links within metacritic)
    validLinks = []
    for link in linkList:
        if 'metacritic' not in link and '.com' in link or 'twitter' in link:
            continue
        else:
            validLinks.append(link)
        
    # Lists all links that must be ignored!
    mc = 'http://www.metacritic.com/'
    mcGame= 'http://www.metacritic.com/game/'
    ignoreList = [mc + 'music', mc + 'tv', mc + 'movie', mcGame + 'pc', mcGame + 'ios', mcGame + 'playstation-3', 
    mcGame + 'xbox', mcGame +'wii-u', mcGame + '3ds', mcGame + 'playstation-vita', mcGame + 'wii', mcGame + 'psp', mcGame + 'legacy']

    # # Random walk through valid links, writes every link that is a review to a new file
    goodLinks = []
    checkAgain= []
    newLinkFile = open(directory + "/" + fileName + "-links.txt", 'w')
    for link in validLinks: 
        if "http" not in link:
            newLink = 'http://www.metacritic.com'+link 
        else:
            newLink= link 
        try:
            followLink= URLopener().open(newLink)
            checkLink= followLink.read()
            soupIt= BeautifulSoup(checkLink)
            if 'Reviews - Metacritic' in soupIt.title.string and 'Metascore' and 'Release Date' and 'User Score' in soupIt.get_text() and newLink not in ignoreList:
                print "Wrote to file good link: " +  newLink + '\n'
                newLinkFile.write(newLink + '\n') 
            else: 
                print 'Will check again: ' + newLink + '\n'
                checkAgain.append(newLink)
        except IOError:
            print "Link no longer valid: " + newLink + '\n'
    # Removes duplicates
    checkList= list(set(checkAgain))
    # Shuffle list of links
    random.shuffle(checkList)
    crawl(checkList[0])

crawl(metacritic)