import requests
import pandas as pd
header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}
list = []
next_page = 'NTU%3D'
while(True):
    response = requests.get(f'https://www.rottentomatoes.com/cnapi/browse/movies_at_home?after={next_page}', headers=header)
    data = response.json()

    movies = data.get('grid', {}).get('list', [])
    for movie in movies:
        movie_name = movie.get('title', 'Not Available')
        year = movie.get('releaseDateText', 'Not Available').split(',')[-1].strip()
        crit_score_percent = movie.get('criticsScore', {}).get('scorePercent', 'Not Available')
        crit_sent = movie.get('criticsScore', {}).get('sentiment', 'Not Available')
        audience_score_percent = movie.get('audienceScore', {}).get('scorePercent', 'Not Available')
        audience_sent = movie.get('audienceScore', {}).get('sentiment', 'Not Available')
        dict = {
            'Movie_name' : movie_name,
            'Year' : year,
            'Critics_Score_Percent' : crit_score_percent,
            'Critics_Score_Sentiment' : crit_sent,
            'Audience_Score_Percent' : audience_score_percent,
            'Audience_Score_Sentiment' : audience_sent,
        }
        list.append(dict)
        print(dict)
    next_page = data.get('pageInfo', {}).get('endCursor', 'NOT_FOUND')
    if next_page == 'NOT_FOUND':
        break
df = pd.DataFrame(list)
df.to_csv("rotten.csv", index=False)
print("=============Scraping Done=============")
# movie_name = data['grid']['list'][0]['title']
# year = data['grid']['list'][0]['releaseDateText'].split(',')[-1].strip()
# crit_score_percent = data['grid']['list'][0]['criticsScore']['scorePercent']
# crit_sent = data['grid']['list'][0]['criticsScore']['sentiment']
# audience_score_percent = data['grid']['list'][0]['audienceScore']['scorePercent']
# audience_sent = data['grid']['list'][0]['audienceScore']['sentiment']
# print(audience_score_percent)
# print(audience_sent)
