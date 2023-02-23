from selectorlib import Extractor
import requests 
import json 
from time import sleep

keyword_from_user = input("Give the keyword")
keyword_from_user = keyword_from_user.replace(' ', '')
url = "www.amazon.in/s?k={}".format(keyword_from_user)
#data = requests.get(url)
#print(data.txt)

yaml_extractor = Extractor.from_yaml_file('search_results.yml')
def main_scraper(url):
  #To disguise as a browser
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
  if result.status_code != 200:
        
    print("Request was rejected by amazon. please try again....status code --> ", result.status_code)
        
    return None
    
  return yaml_extractor.extract(result.text) # passing the result from get request to yaml and alligning the data meaningfully
data = main_scraper(url)
print(data)
