import requests
import time

def get_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    return end_time - start_time

print(get_page_load_time('https://www.google.com'))
print(get_page_load_time('https://www.ynet.co.il'))
print(get_page_load_time('https://www.imdb.com'))