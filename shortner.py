# Short version if you want separate file
from main import URLShortener

def quick_shorten(url):
    s = URLShortener()
    return s.shorten_url(url)

def quick_open(code):
    s = URLShortener()
    return s.open_url(code)
