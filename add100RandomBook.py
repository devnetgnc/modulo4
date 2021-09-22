import requests #libreria para hacer peticiones http
import json
from faker import Faker
LOGIN ="cisco"
PASSWORD="Cisco123!"
urlAPI="http://library.demo.local/api/v1/"

urlGetBook = "http://library.demo.local/api/v1/books?includeISBN=true&sortBy=id"

response =requests.get(urlGetBook)

print(response.json())



#Obtener Token
def getAuthToken():
    credenciales =(LOGIN,PASSWORD)
    resp = requests.post(f'{urlAPI}loginViaBasic',auth=credenciales)
    
    if resp.status_code==200:
        return resp.json()["token"]
    else:
        raise Exception(f'Status code {response.status_code} and text{response.text}') 
# Agregar Libros
def addBook(book, apikey):
    resp = requests.post(f'{urlAPI}books',
    headers={
        "Content-type":"application/json",
        "X-API-Key":apikey
    },
    data=json.dumps(book)
    )
    if resp.status_code ==200:
        print(f'Book {book} added.')
    else:
        raise Exception(f'Error code {resp.status_code} and text {resp.text}, while trying to add book {book}')

apikey = getAuthToken()
fake = Faker()

#Probar agregar  libros en forma masiva 
for i in range(108,200):
    fakeTitle = fake.catch_phrase()
    fakeAutor = fake.name()
    fakeISBN =fake.isbn13()
    book={"id":i, "title":fakeTitle,"author":fakeAutor,"isbn":fakeISBN}
    addBook(book,apikey)

           
