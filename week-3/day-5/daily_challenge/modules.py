import requests
import time

def page_load_timer(url):
    before = time.perf_counter()
    r = requests.get(url)
    after = time.perf_counter()
    print(after - before)
    return after - before

page_load_timer('https://google.com')
page_load_timer('https://facebook.com')
page_load_timer('https://x.com')
page_load_timer('https://amazon.com')
page_load_timer('https://whitehouse.gov')

