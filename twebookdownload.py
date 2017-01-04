# !/usr/bin/env python
from __future__ import print_function
from urllib import request
import sys
import os
import time

url = sys.argv[1]

def get_PDF_url(url):
	
	url_parts = url.split('/')
	filename = url_parts[5] + '.PDF' 
	PDF_url = url_parts[0] + '//' + url_parts[2] + '/ebkFiles/' + url_parts[5] + '/' + filename
	
	return PDF_url, filename

def get_book_metadata(url):
	response = request.urlopen(url)
	content = response.read()

def progressbar(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d/%d, MB, %d KB/s" %
                    (percent, progress_size / (1024 * 1024), total_size / (1024 * 1024), speed))
    sys.stdout.flush()


def download_PDF(url, filename):

	req = request.Request(
		url,
		data=None,
		headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
            		  "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}

		)

	response = request.urlretrieve(url, '%s' % (filename), progressbar)

	print('/nDownload Complete!')

PDF_url, filename = get_PDF_url(url)
print(PDF_url)
download_PDF(PDF_url, filename)