import requests
import urllib.parse

starLocation="Buenos Aires"
endLocation="ME"
apikey="in8cjzhG4Hgbv6G57tATnQjAAvviO9Ye"
main_api="https://www.mapquestapi.com/directions/v2/route?"

url = main_api+ urllib.parse.urlencode({"key":apikey,
"from":starLocation,"to":endLocation})
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0 :
    print(f'API status {json_status} succefull route call')
else:
    print(f'API status {json_status} error route call')     

