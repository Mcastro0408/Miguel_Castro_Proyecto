class Planetas:
    def __init__(self, nombre, periodo_de_orbita, periodo_de_rotacion, poblacion, clima, personajes, apariciones):
        self.nombre = nombre
        self.periodo_de_orbita = periodo_de_orbita
        self.periodo_de_rotacion = periodo_de_rotacion
        self.poblacion = poblacion
        self.clima = clima
        self.persoanjes = personajes
        self.apariciones = apariciones
    def show_attr(self):
        print(f'nombre: {self.nombre}')
        print(f'periodo de orbita: {self.periodo_de_orbita}')
        print(f'poblacion: {self.poblacion}')
        print(f'clima: {self.clima}')
        print(f'personajes: {self.persoanjes}')
        print(f'aparicones: {self.apariciones}')
        