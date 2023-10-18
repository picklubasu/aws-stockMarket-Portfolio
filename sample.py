# import requests
# import json

# request_header = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' }
# request_url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20TOTAL%20MARKET'

# response = requests.get(url = request_url, headers = request_header)
# response.json()

import requests
import json

request_header = { 
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cookie':'nsit=KAEm6-ZwUJoZPe2AaT-zY0Pf;_gid=GA1.2.1219990500.1697650189;_ga=GA1.1.1807715373.1695384184;nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY5NzY1NTQ3MSwiZXhwIjoxNjk3NjYyNjcxfQ.vZ6naUyh85UqEsf6KPZBjPb5Fy-xvUgIt_P9jtl6FLM;7EF30E83608027A51B55C33AE8B0BDBB~000000000000000000000000000000~YAAQI0w5F2cTiUGLAQAA7bXVQxWEEmovtf48sg7qyqCmhQ4N2Bs13yG2s9Pg3FojWRPaqklBJesQ7DVerUZl95KQmgOBJtPU3072Qt2jxk7fUbMzMKLg+x2ZE4rpGEZjWh4m15ZNZ65G+K+8ka/g2AL0aBzwW2wMZnE8TePxJeEIGtfd8lo9DEYuVy5Xil05rPfVtJuG8wV5fKCjp/YLAxIXyVEbYH9Eiy198lEg4zwyJE6zXgLnqc/GclMX6FaYWzBe4Rt9szSGn05ZneONSw7EQUNHGqzSwHanUJXs6taJULUpehd6kx4TkFDEY7kV661UEC8LKtNpL+4dqTkNFVL0pJsUf9fzkI4t/Z2v64zTNLkzfA8XE1n5pFZ9QT5Zos4d8fp3SIq1MFzdLbIjRA/E8pFwba3+ZDHo/Zl0AI5nmJ2e8reScojrJMno6tV97gzwcZLhv6YEZEN5uPjbo64GzZPzqbTN5iDEWWaJkHSO3JjXP4sB/cjOWXUrxWm5gsdyi0e4+JPVE9Nh6GOc+e2UMws=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' 
}
request_url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20TOTAL%20MARKET'

response = requests.get(url = request_url, headers = request_header)
print(response.json())
