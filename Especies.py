class Especies:
    def __init__(self, id, nombre_especie, planeta_origen, lengua_materna, personajes, apariciones):
        self.id= id
        self.nombre_de_la_especie = nombre_especie
        self.planeta_origen = planeta_origen
        self.lengua_materna = lengua_materna
        self.personajes = personajes
        self.apariciones = apariciones
    def show_attr(self):
        print(f'id: {self.id}')
        print(f'nombre: {self.nombre_de_la_especie}')
        print(f'planeta de origen: {self.planeta_origen}')
        print(f'legua materna: {self.lengua_materna}')
        print(f'personajes: {self.personajes}')
        print(f'apariciones: {self.apariciones}')        
