import requests

keyword_from_user = input("Give the keyword")
keyword_from_user = keyword_from_user.replace(' ', '')
url = "www.amazon.in/s?k={}".format(keyword_from_user)
data = requests.get(url)
print(data.txt)


