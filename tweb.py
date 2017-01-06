# !/usr/bin/env python
from __future__ import print_function
from urllib import request
from bs4 import BeautifulSoup
import requests
import sys
import os
import time
import re

url = sys.argv[1]
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            		  "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}

def get_PDF_url(url):
	
	url_parts = url.split('/')
	filename = url_parts[5] + '.PDF' 
	PDF_url = url_parts[0] + '//' + url_parts[2] + '/ebkFiles/' + url_parts[5] + '/' + filename
	
	return PDF_url, filename

content = requests.get(url, headers)
soup = BeautifulSoup(content.text, 'lxml')
title_raw = soup.findAll("h2")[1].text.split('\r\n')[1]
title = re.sub('\W+', '', title_raw)
PDF_url, filename = get_PDF_url(url)
print("Downloading book: ", title)

# download_PDF(PDF_url, filename)
os.system("you-get -O {0}.pdf {1}".format(title,PDF_url))
