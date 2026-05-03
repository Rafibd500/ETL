import pandas as pd
import requests
header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}
prod_list = []
category_response = requests.get('https://pharmeasy.in/api/home/fetchCategories')
cat_res = category_response.json()
categories=cat_res.get('data', {}).get('categories', [])
for category in categories:
    cat_id = category.get('id', '')
    i = 1
    category_name = category.get('name')
    while(True):
        response = requests.get(f'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId={cat_id}&page={i}')
        print(f'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId={cat_id}&page={i}')
        data = response.json()
        if(data.get('data') == {}):
            break
        products = data.get('data', {}).get('products', [])
        print(len(products))
        for product in products:
            # print(product)
            # 4.1 Product-Level Fields
            name = product.get('name', 'Not Found')
            brand_name = product.get('manufacturer', 'Not Found')
            price = product.get('mrpDecimal', 'Not Found')
            discount_percent = product.get('discountPercent', 'Not Found')
            # img_url = product.get('images', [])[0]
            # sub_category = 
            
            if not product.get('ratingDetails', {}):
                rating = 'Not found'
            else:
                rating = product.get('ratingDetails', {}).get('value', -1)
                rating = round(rating, 2)
                num_of_review = product.get('ratingDetails', {}).get('count', -1)
            
            availability = 'In Stock' if product.get('isAvailable') == True else 'Out Of Stock' 

            # 4.2 Additional Fields
            # p_id = product.get('productId', 'Not Found')
            # pack_size = 
            # ingredients = 
            # usage_instructions = 
            # manufacturer_name = 
            # expiry_info = 
            # deliver_time = 

            # 4.3 Platform-Level Fields
            # total_product = 
            # page_number = i
            # Filters (Price range, brands, etc.)
            dict = {
                'Product Name':name,
                'Brand':brand_name,
                'Price' : price,
                'Discount': discount_percent,
                'Rating' : rating,
                'Review' : num_of_review,
                'Catergory' : category_name,
                'Availability' : availability,
            }
            print(dict)
            prod_list.append(dict)
        i+=1
df = pd.DataFrame(prod_list)
df.to_csv("pharm_easy.csv", index=False)
print("=========Successfully Scraped=========")