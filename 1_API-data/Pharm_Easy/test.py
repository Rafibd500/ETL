import requests
import pandas
i = 1
while(True):
    data = requests.get(f'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=877&page={i}')
    dt = data.json()
    if(dt.get('data') == {}):
        break
    # products = dt.get('data').get('products')
    # for prod in products:
    #     print(prod.get('name', ''))
    print(i)
    print(dt)
    
    i+=1