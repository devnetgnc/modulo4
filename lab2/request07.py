import requests
import urllib.parse

from requests import status_codes
apikey="in8cjzhG4Hgbv6G57tATnQjAAvviO9Ye"
main_api="https://www.mapquestapi.com/directions/v2/route?"

def millas_to_km(millas):
    return millas * 1.61

def galones_to_litros(galones):
    return galones * 3.78

while True:

    origen= input('Ingrese el punto de partida: ')
    if origen =='q' or origen == 'quit':
        break

    dest = input('Ingrese el punto de destino: ')

    if dest =='q' or dest =='quit':
        break
    url= main_api + urllib.parse.urlencode({"key":apikey, 
    "from":origen, "to": dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status ==0:
        print(f'API status: {json_status} succeful route call')
        print("=============================================")
        print(f'Direccion Origen: {origen}, destino: {dest}')
        print(f'Duracion viaje {json_data["route"]["formattedTime"]}')
        print(f'Millas: {json_data["route"]["distance"]}')
        print(f'Kilometros: {millas_to_km(json_data["route"]["distance"]):.2f}')
        print(f'Fuel used (Gal): {json_data["route"]["fuelUsed"]}')
        print(f'Fuel used (Ltrs): {galones_to_litros(json_data["route"]["fuelUsed"]):.2f}')
        for i in json_data["route"]["legs"][0]["maneuvers"]:
            print(f"{i['narrative']}, {millas_to_km(i['distance']):.2f} Km.")
        print("=============================================")
    elif json_status == 402:
        print("**********************************************")
        print(f"Status code {json_status} Invalid user input for one or both locations.")
        print("**********************************************")
    elif json_status ==611:
        print("**********************************************")
        print(f"Status code {json_status} At least two locations required.")
        print("**********************************************")
    else:
        print("**********************************************")
        print(f"Status code {json_status} refer to:.")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes/")
        print("**********************************************")
