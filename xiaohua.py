import requests
import re

def getHtml(url):
    html = requests.get(url)
