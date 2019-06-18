from clases import *
import json
from math import inf as infinito

with open('calles.txt') as json_file:
    calles = json.load(json_file)


class Simulacion:
    def __init__(self, grid):
        self.camiones_chicos = []
        self.camion_grande = None
        self.grid = grid
        self.calles = None
        self.basura_recogida_limpiaexpress = 0

    def load_data(self,calles):
        #SE CREAN Y SE AÑADEN LOS CAMIONES CHICOS
        for cuadrante in calles_en_cuadrantes:
            self.camiones_chicos.append(Camion_chico(cuadrante, calles_en_cuadrantes[cuadrante]))
        #SE CREA Y SE AÑADE EL CAMION GRANDE
        self.camion_grande = Camion_grande()
        self.calles = self.grid.calles
    
    def termino_simulacion(self):
        pass
    
    def limpia_express(self):
        for calle in self.calles:
            if calle.basura_actual >= 12:
                self.basura_recogida_limpiaexpress += calle.basura_actual
                calle.basura_actual = 0

    def dia_simulacion(self):
        tiempo_simulacion = 0
        self.grid.generar_basura()
        print(self.grid)
        self.grid.mapa()
        for camion in self.camiones_chicos:
            camion.inicio_dia()
            camion.tiempo_traslado_cuadrante(tiempo_simulacion)
        while tiempo_simulacion < 11 * 3600:
            tiempo_minimo = infinito
            camion_actual = None
            for camion in self.camiones_chicos:
                if camion.tiempo_siguiente_evento < tiempo_minimo:
                    tiempo_minimo = camion.tiempo_siguiente_evento
                    camion_actual = camion
            if self.camion_grande.tiempo_siguiente_evento < tiempo_minimo:
                tiempo_minimo = self.camion_grande.tiempo_siguiente_evento
                camion_actual = self.camion_grande
            tiempo_simulacion = tiempo_minimo
            
            if isinstance(camion_actual, Camion_chico): #Si el camion que realiza el siguiente evento es chico:
                print("EVENTO CAMIÓN CHICO ID {}: {} AT {}".format(camion_actual.id, camion_actual.status, tiempo_simulacion))
                if camion_actual.status == "RECOLECTANDO":
                    camion_actual.tiempo_traslado_acopio(tiempo_simulacion)
                elif camion_actual.status == "YENDO A CUADRANTE":
                    camion_actual.tiempo_en_recolectar(tiempo_simulacion)
                elif camion_actual.status == "YENDO A VACIAR":
                    self.camion_grande.cola_vaciado.append(camion_actual)
                    camion_actual.status = "COLA VACIADO"
                    camion_actual.tiempo_siguiente_evento = infinito
                    if len(self.camion_grande.cola_vaciado) == 1 and self.camion_grande.status == "CENTRO DE ACOPIO":
                        self.camion_grande.tiempo_siguiente_evento = tiempo_simulacion
                elif camion_actual.status == "VACIANDO":
                    self.camion_grande.cola_vaciado.pop(0)
                    camion_actual.tiempo_traslado_cuadrante(tiempo_simulacion)
                    if len(self.camion_grande.cola_vaciado) >= 1 and self.camion_grande.status == "CENTRO DE ACOPIO":
                        self.camion_grande.tiempo_siguiente_evento = tiempo_simulacion

            else:  #Si el camion que realiza el siguiente evento es grande:
                print("EVENTO CAMIÓN GRANDE: {} AT {}".format(camion_actual.status, tiempo_simulacion))
                if camion_actual.status == "VACIADO":
                    self.camion_grande.status = "CENTRO DE ACOPIO"
                    if len(camion_actual.cola_vaciado) != 0:
                        self.tiempo_siguiente_evento = tiempo_simulacion
                elif camion_actual.status == "CENTRO DE ACOPIO":
                    camion_actual.descarga_camion_chico(tiempo_simulacion)
        aux = 0 
        for camion in self.camiones_chicos: #hay que cambiar esto.
                                            #le estoy metiendo a la mala toda la basura de los camiones que están esperando o recolectando.
            self.camion_grande.basura_actual += camion.basura_actual
            camion.basura_actual = 0
            print("basura actual {} tiempo evento {} basura total recogida {}".format(camion.basura_actual,
                                                                            camion.tiempo_siguiente_evento, camion.basura_total_recogida))
            aux += camion.basura_total_recogida

        print("-----  BASURA TOTAL RECOGIDA  {} -----".format(aux))

        for camion in self.camion_grande.cola_vaciado: # esto es para que el camion grande vaya a dejar la basura
            self.camion_grande.descarga_camion_chico(tiempo_simulacion)


        self.camion_grande.ida_vaciado(tiempo_simulacion)      
        print("BASURA TOTAL CAMION GRANDE: {}".format(self.camion_grande.basura_total))
        print(self.grid)
        self.limpia_express()
        self.grid.mapa()







grid = Grid()
simulacion = Simulacion(grid) 

calles_en_cuadrantes = {}  #DICCIONARIO CON LAS CALLES ORDENADAS POR CUADRANTE,
for x in range (1,18):
    calles_en_cuadrantes[x] = []
    for data in calles:
        if calles[data]["cuadrante"] == x:
            calle = Calle(data, calles[data]["comienza"][1], calles[data]["comienza"][0], calles[data]["termina"][1], calles[data]["termina"][0], calles[data]["cuadrante"], calles[data]["subcuadrante"])
            calles_en_cuadrantes[x].append(calle)
            grid.add_calle(calle)

simulacion.load_data(calles_en_cuadrantes)

for camion in simulacion.camiones_chicos:
    camion.definir_orden_recoleccion()
simulacion.dia_simulacion()
