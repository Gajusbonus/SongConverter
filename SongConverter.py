#!/usr/bin/env python

# Maakt van een OpenSong-bestand Chrodpro-bestand
from xml.etree import ElementTree as ET
import argparse
import re						#regular expressions
import sys
import xml.dom.minidom as minidom

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", help="Voor meer gedetaileerde uitvoer", action="store_true")
    parser.add_argument('filename')
    parser.parse_args()
    args = parser.parse_args()
    return args


def main():
    Text = ""
    args = get_args()
    file=open(args.filename,'r')
    s=file.read()
    Tag = "title" 
    title=getText(Tag,s)
    Tag = "author" 
    author=getText(Tag,s)
    #print "We are done now"'\n'
    Tag = "lyrics" 
    lyrics=getText(Tag,s)
    print title,' by ',author
    print lyrics
    file.close()
    q=find_str(s,'[V]')
    print q

def getText(Tag,s):
        doc = minidom.parseString(s)
        i = 0
        for topic in doc.getElementsByTagName(Tag):
           Text= doc.getElementsByTagName(Tag)[i].firstChild.nodeValue
           i +=1
        return (Text)

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1


if __name__ == '__main__':
    main()


