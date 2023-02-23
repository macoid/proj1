from selectorlib import Extractor
import requests 
import json 
from time import sleep


# an extractor which reads from yaml and alligns the result meaning fully
yaml_extractor = Extractor.from_yaml_file('website_metadata.yml')
user_input = input(" Please input the product name you want to search : ")
user_input = user_input.replace(' ', '')
url = "https://www.amazon.in/s?k={}/".format(user_input)
def main_scraper(url):  
    # to disguise as a browser
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    
    print("Extracting data from ", url)
    result = requests.get(url, headers=headers)
    # Checking if the request is rejected
    if result.status_code != 200:
        print("Request blocked by amazon status code : ", result.status_code)
        return None
    # Passing the api result to yaml for alligning it meaningfully
    return yaml_extractor.extract(result.text)



def display_product_information(data):
    # displaying results based on the yaml configuration
    for product in data['products']:
        
        print("Product name --> ", product['title'])
        print("Product price --> ", product['price'])
        print("Product rating --> ", product['rating'])
        print("To order this product use --> ", "www.amazon.in" + product['url'])
        



def main():
    
    flag = None # using this to retry in case request is blocked by amazon due to so many requests
    while flag != True:
        scraped_data = main_scraper(url)
        if scraped_data:
            display_product_information(scraped_data)
            flag = True
        else:
            
            flag = False
        

main()


