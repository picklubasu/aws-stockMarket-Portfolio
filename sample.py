# import requests
# import json

# request_header = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' }
# request_url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20TOTAL%20MARKET'

# response = requests.get(url = request_url, headers = request_header)
# response.json()

import requests
import json

request_header = { 
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' 
}
request_url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050'

response = requests.get(url = request_url, headers = request_header)
print(response.status_code)
print(response.json())
