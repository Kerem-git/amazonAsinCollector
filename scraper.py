import requests

user_agent = {'User-agent': 'Mozilla/5.0'}
url ="https://www.amazon.ca/s?me=A2HFA2QNCUMBI8&marketplaceID=A2EUQ1WTGCTBG2" #str(input("Url: "))
r = requests.get(url,headers=user_agent).text

print(r)