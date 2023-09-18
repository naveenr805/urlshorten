import pyshorteners 
url=input('enter url')

def shorten(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))
shorten(url)