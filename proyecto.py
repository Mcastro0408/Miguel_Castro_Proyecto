import requests 
from Peliculas import Peliculas
from Planetas import Planetas
from Especies import Especies

def films_data_base():
    resp=requests.get("https://www.swapi.tech/api/films")
    return resp.json()

def people_data_base():
    resp=requests.get("https://www.swapi.tech/api/people?page=2&limit=90")
    return resp.json()

def species_data_base():
    resp=requests.get("https://www.swapi.tech/api/species?page=2&limit=37")
    return resp.json()

def planets_data_base():
    resp=requests.get("https://www.swapi.tech/api/planets?page=1&limit=60")
    return resp.json()


def search_people(db, name):
    if response.status_code == 200:
        find_number=0
        for people in db['results']:
            if name in people['name']:
                find_number+=1
                id=''
                for lu in people['url']:
                    if lu.isdigit():
                        id=id+lu
                        id=id[1:len(id)]
                        print(people["name"], "ID: ",id)
    
    if find_number:
        print(f"\nSe encontraron {find_number} resultados.")
    else:
        print("\nNo se encontraron resultados ")

response=people_data_base()
while True:
    option=int(input("""
Introduzca una opcion:
    [0] Salir.
    [1] Buscar personajes.
    [2] Mostrar lista de peliculas.
    [3] Mostrar lista de planetas.
    [4] Mostrar lista de especies.
-------->"""))
    if option == 0:
        break
    elif option == 1:
        name=input("Introduzca el nombre: ")
        search_people(response,name)
    
    elif option == 2:
        mostrar_peliculas()
        
    elif option == 3:
        mostrar_planetas()

    elif option == 4:
        mostrar_especies()

    else:
        print("Opcion invalida. Intente nuevamente: ")

print("Hasta luego ")
    
