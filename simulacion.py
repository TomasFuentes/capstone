from clases import *
import json

with open('calles.txt') as json_file:
    calles = json.load(json_file)

grid = Grid()
for data in calles:
    grid.add_calle(data, calles[data])
    
calles_en_cuadrantes = {}  #DICCIONARIO CON LAS CALLES ORDENADAS POR CUADRANTE,
             #ES DECIR, La entrada 1 tiene una lista con todas las calles correspondientes al cuadrante 1.
for x in range (1,18):
    calles_en_cuadrantes[x] = []
    for data in calles:
        if calles[data]["cuadrante"] == x:
            calles_en_cuadrantes[x].append(Calle(data, calles[data]["comienza"][1], calles[data]["comienza"][0], calles[data]["termina"][1], calles[data]["termina"][0], calles[data]["cuadrante"], calles[data]["subcuadrante"]))

class Simulacion:
    def __init__(self):
        self.camiones_chicos = []
        self.camiones_grandes = []

    def load_data(self,calles):
        #SE CREAN Y SE AÑADEN LOS CAMIONES CHICOS
        for cuadrante in calles_en_cuadrantes:
            self.camiones_chicos.append(Camion_chico(cuadrante, calles_en_cuadrantes[cuadrante]))
        #SE CREA Y SE AÑADE EL CAMION GRANDE
        self.camiones_grandes.append(Camion_grande())

    def minimo_en_llegar_cuadrante(self):
        minimo = list()
        for camion in self.camiones_chicos:
            if camion.status == "standby":
                minimo.append((camion.id, camion.tiempo_desde_origen(camion.minimo_cuadrante())))
            else:
                minimo.append((camion.id, infinito))
        return min(minimo, key = lambda t: t[1])
    
    def termino_simulacion(self):
        pass
    
    def inicio_simulacion(self):
        t = 0
        while t < 1000:
            minimo = [self.minimo_en_llegar_cuadrante()]
        self.termino_simulacion()

simulacion = Simulacion()
simulacion.load_data(calles_en_cuadrantes)
simulacion.inicio_simulacion()
simulacion.camiones_chicos[0].definir_orden_recoleccion()
print(simulacion.minimo_en_llegar_cuadrante())
