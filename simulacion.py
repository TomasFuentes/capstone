from clases import *
import json

grid = Grid()
calles_en_cuadrantes = {}  #DICCIONARIO CON LAS CALLES ORDENADAS POR CUADRANTE,
             #ES DECIR, La entrada 1 tiene una lista con todas las calles correspondientes al cuadrante.
for x in range (1,18):
    calles_en_cuadrantes[x] = []
with open('calles.txt') as json_file:
    calles = json.load(json_file)

print(calles_en_cuadrantes)
for data in calles:
    grid.add(data, calles[data])
    cuadrante_calle = calles[data]["cuadrante"]
    calles_en_cuadrantes[cuadrante_calle].append(Calle(data, calles[data]["comienza"][1], calles[data]["comienza"][0], calles[data]["termina"][1],
                                                       calles[data]["termina"][0], calles[data]["cuadrante"], calles[data]["subcuadrante"]))
print(grid)
grid.generar_basura()
print(grid)
for x in grid.calles:
    print(x)


class Simulacion:
    def __init__(self):
        self.camiones_chicos = []


    def inicio_simulacion(self,calles):
        for cuadrante in calles:
            self.camiones_chicos.append(Camion_chico(calles[cuadrante]))


simulacion = Simulacion()
simulacion.inicio_simulacion(calles_en_cuadrantes)

for camion in simulacion.camiones_chicos:
    print(camion.calles_a_recolectar)