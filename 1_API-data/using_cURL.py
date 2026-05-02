import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'DNT': '1',
    'Referer': 'https://www.rottentomatoes.com/browse/movies_at_home/?page=2',
}

params = {
    'after': 'Mjc=',
}

response = requests.get('https://www.rottentomatoes.com/cnapi/browse/movies_at_home', params=params, headers=headers)

print(response.json())
data = response.json()
print(data)