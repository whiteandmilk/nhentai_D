#!/usr/bin/python
# -*- coding: utf-8 -*-
# Please create a new folder and put it in

from bs4 import BeautifulSoup
import requests

# import os
# import sys

# comicUrl = sys.argv[1]

def downloadImg(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as code:
        code.write(r.content)


comicUrl = 'http://nhentai.net/g/140078/'
response01 = requests.get(comicUrl).content
html01 = BeautifulSoup(response01, 'html.parser')
title01 = html01.h2.string
print title01
gList01 = html01.findAll('a', class_='gallerythumb')
pages01 = len(gList01)
print
print pages01, 'pages'

page01url = comicUrl + '1/'
response02 = requests.get(page01url).content
html02 = BeautifulSoup(response02, 'html.parser')
img01Url = html02.find(id='image-container'
                       ).contents[1].contents[1].get('src')
iut = img01Url.split('/')
imgurl01 = iut[2] + '/' + iut[3] + '/' + iut[4] + '/'
imgurl01 = 'http://' + imgurl01
filetype01 = '.jpg'

i = 1
while i <= pages01:
    filename = str(i) + filetype01
    imgUrl = imgurl01 + filename
    print 'Downloading no.', i, ' page'
    downloadImg(imgUrl, filename)
    i = i + 1

print 'Downloading finish'

# os.system("pause")