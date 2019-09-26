"""
<html_downloader.py>
Download content from given url. Only handle HTTP CODE 200
"""
from urllib import request

class HtmlDownLoader(object):
    def download(self, url):
        if url is None:
            return
        response = request.urlopen(url)
        if response.getcode() != 200:
            return
        return response.read()