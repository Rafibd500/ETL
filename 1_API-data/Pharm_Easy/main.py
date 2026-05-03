import pandas as pd
import requests
header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}
prod_list = []
category_response = requests.get('https://pharmeasy.in/api/home/fetchCategories')
cat_res = category_response.json()
categories=cat_res.get('data', {}).get('categories', [])
for cat in categories:
    cat_id = cat.get('id', '')
    i = 1
    category_name = 
    while(True):
        response = requests.get(f'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId={cat_id}&page={i}')
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
            price = 
            discount_percent = 
            description = 
            img_url = 
            # cat
            sub_category = 
            rating = 
            num_of_review = 
            availability = 

            # 4.2 Additional Fields
            # SKU / Product ID
            p_id = 
            # Pack Size (e.g., 100ml, 10 tablets)
            pack_size = 
            # Ingredients / Composition
            ingredients = 
            # Usage Instructions
            usage_instructions = 
            # Manufacturer Name
            manufacturer_name = 
            # Expiry Information
            expiry_info = 
            # Delivery Time
            deliver_time = 

            # 4.3 Platform-Level Fields
            # Category Name
            category_name
            # Total Number of Products
            total_product = 
            # Pagination (Page number)
            page_number = i
            # Filters (Price range, brands, etc.)
        i+=1