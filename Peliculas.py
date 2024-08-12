class Peliculas:
    def __init__(self, titulo, episodio, fecha_de_lanzamiento, opening_crawl, director):
        self.titulo = titulo
        self.episodio = episodio
        self.fecha_de_lanzamiento = fecha_de_lanzamiento
        self.opening_crawl = opening_crawl
        self.director = director
    def show_attr(self):
        print(f'titulo: {self.titulo}')
        print(f'episodio: {self.episodio}')
        print(f'fecha de lanzamiento: {self.fecha_de_lanzamiento}')
        print(f'opening: {self.opening_crawl}')
        print(f'director: {self.director}')
        
