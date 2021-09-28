import requests
import urllib.parse

from requests import status_codes
apikey="in8cjzhG4Hgbv6G57tATnQjAAvviO9Ye"
main_api="https://www.mapquestapi.com/directions/v2/route?"

while True:

    origen= input('Ingrese el punto de partida: ')
    dest = input('Ingrese el punto de destino: ')
    url= main_api + urllib.parse.urlencode({"key":apikey, 
    "from":origen, "to": dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status ==0:
        print(f'API status: {json_status} succeful route call')
        print(json_data)