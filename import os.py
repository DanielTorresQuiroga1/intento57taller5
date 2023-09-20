import os
import random

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    # Aquí irían todos los métodos 
    # pero ahora usando self.mapa, self.inicio, etc.

    def jugar(self):
        # Lógica para jugar
        pass

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        mapa, inicio, fin = self.cargar_mapa()
        super().__init__(mapa, inicio, fin)

    def cargar_mapa(self):
        archivos = os.listdir(self.path_a_mapas)
        archivo_elegido = random.choice(archivos)
        path_completo = f"{self.path_a_mapas}/{archivo_elegido}"
        
        with open(path_completo, 'r') as archivo:
            dimensiones = archivo.readline().strip().split('x')
            ancho, alto = int(dimensiones[0]), int(dimensiones[1])
            inicio = tuple(map(int, archivo.readline().strip().split(',')))
            fin = tuple(map(int, archivo.readline().strip().split(',')))
            mapa = archivo.read().strip()
        
        return mapa, inicio, fin

if __name__ == "__main__":
    juego = JuegoArchivo("path_a_tus_mapas")
    juego.jugar()