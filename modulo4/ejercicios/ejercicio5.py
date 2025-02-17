import requests 

url="https://pokeapi.co/api/v2/pokemon"

response=requests.get(url)

if response.status_code==200:
    data=response.json()
    #print(data.keys())
    resultados=data['results']
    print("Elige tu pokemon:")
    for i in resultados:
        id=i['url'].split('/')[-2]
        print(f"{id}.{i['name']}")
    pokemon=input("que pokemon eliges: ")
    responsev2=requests.get(f"{url}/{pokemon}/")
    if responsev2.status_code==200:
        pokemonElegido=responsev2.json()
        menssage=f"Felicidades elegiste a {pokemonElegido['name']} que cuenta con {pokemonElegido['base_experience']} exp"
        print(menssage)
