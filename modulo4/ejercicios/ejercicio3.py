import requests
from bs4 import BeautifulSoup

url="https://es.wikipedia.org/wiki/Wikipedia_en_espa%C3%B1ol"
response=requests.get(url)

if response.status_code==200:
    print("es correcto")
    
    data =BeautifulSoup(response.content,'html.parser')
    title=data.title.string
    print(title)
    ##print(data.prettify())

    
    dataIds=data.find(id='mw-content-text')
    print(dataIds)
else:
    print('error',response.status_code)