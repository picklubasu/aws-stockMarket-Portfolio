import requests
import json

text = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

r = requests.get('https://www.nseindia.com/', headers=text,allow_redirects=False)

for c in r.cookies:
    print(c.name +"==>>", c.value)
