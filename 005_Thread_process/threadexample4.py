import concurrent.futures
import urllib.request

URLS = ['http://httpbin.org', 'http://example.com/', 'https://api.github.com/']

def load_url(url):
    with urllib.request.urlopen(url, timeout=60) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    for url, data in zip(URLS, executor.map(load_url, URLS)):
        print('%r page is %d bytes' % (url, len(data)))