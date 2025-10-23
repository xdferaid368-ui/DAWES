class Videojuego:
    def __init__(self, titulo, distribuidora, anio):
        self.titulo = titulo
        self.distribuidora = distribuidora
        self.anio = anio
    def __str__(self):
        return f"{self.titulo} de la distribuidora {self.distribuidora} en el año {self.anio}"

class BibliotecaVidj:
    def __init__(self):
        self.lista = []
    
    def nuevo(self, videojuego):
        self.lista.append(videojuego)
    
    def mostrar(self):
        print("Listado de videojuegos:")
        for p in self.lista:
            print(f"- {p}")
    
    def añadir_videojuego(self):
        titulo = input("Introduce el título del videojuego que quiere añadir : ")
        distribuidora = input("Introduce la distribuidora: ")
        anio = int(input("Introduce el año de lanzamiento: "))
        nuevo_juego = Videojuego(titulo, distribuidora, anio)
        self.nuevo(nuevo_juego)
        print(f"Videojuego añadido: {nuevo_juego}")
    
    def buscarvidj(self) -> Videojuego:
        titulo = input("Introduzca el nombre del videojuego a buscar: ")
        for videojuego in self.lista:
            if videojuego.titulo.lower() == titulo.lower():
                print(f"Videojuego encontrado: {videojuego}")
                return videojuego
        print("El videojuego no está en la biblioteca de juegos")
        return None


# Crear videojuegos
videojuego1 = Videojuego('Pokemon', 'Nintendo', 1998)
videojuego2 = Videojuego('Bioshock', 'Valve', 2004)

Biblioteca = BibliotecaVidj()
Biblioteca.nuevo(videojuego1)
Biblioteca.nuevo(videojuego2)


Biblioteca.mostrar()
Biblioteca.añadir_videojuego()  
Biblioteca.buscarvidj()

