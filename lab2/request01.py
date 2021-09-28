import requests
import urllib.parse

starLocation="Buenos Aires"
endLocation="Mendoza"
apikey="in8cjzhG4Hgbv6G57tATnQjAAvviO9Ye"
main_api="https://www.mapquestapi.com/directions/v2/route?"

url = main_api+ urllib.parse.urlencode({"key":apikey,
"from":starLocation,"to":endLocation})

print(f'URL: {url}')
response = requests.get(url)
print(response.json())