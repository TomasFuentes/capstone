from scipy.stats import halfgennorm
import numpy as np
import matplotlib.pyplot as plt
import json
from math import inf as infinito

class Grid:
    def __init__(self):
        self.calles = list()

    def __str__(self):
        basura = 0
        contador = 0
        for calle in self.calles:
            basura += calle.basura_actual
            contador += 1
        return "En la comuna hay {} kilogramos de basura distribuídos en {} calles".format(basura, contador)
    
    def mapa(self):
        x = list()
        y = list()
        contador = 0
        for calle in self.calles:
            x.append(calle.inicio_x)
            x.append(calle.termino_x)
            x.append(contador)
            y.append(calle.inicio_y)
            y.append(calle.termino_y)
            y.append(contador)
            contador += 1
        for i in range(0, len(x), 3):
            if self.calles[x[i+2]].basura_actual > 12:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#ff00ff')
            elif self.calles[x[i+2]].basura_actual > 11:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#260206')
            elif self.calles[x[i+2]].basura_actual > 10:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#360000')
            elif self.calles[x[i+2]].basura_actual > 9:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#400001')
            elif self.calles[x[i+2]].basura_actual > 8:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#5f0000')
            elif self.calles[x[i+2]].basura_actual > 7:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#911202')
            elif self.calles[x[i+2]].basura_actual > 6:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#ab2700')
            elif self.calles[x[i+2]].basura_actual > 5:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#d85500')
            elif self.calles[x[i+2]].basura_actual > 4:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#f97e03')
            elif self.calles[x[i+2]].basura_actual > 3:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#ffb339')
            elif self.calles[x[i+2]].basura_actual > 2:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#fcff76')
            elif self.calles[x[i+2]].basura_actual > 1:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#fffdbd')
            elif self.calles[x[i+2]].basura_actual > 0:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#fcfdf3')
            else:
                plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#ffffff')
        return plt.show()

    def add_calle(self, calle):
        self.calles.append(calle)

    def generar_basura(self):
        for calle in self.calles:
            calle.basura_actual += halfgennorm.rvs(calle.beta, calle.loc, calle.scale, size=1)

class Calle:
    beta = 24.55
    loc = 1.00
    scale = 3.97

    def __init__(self, nombre, inicio_x, inicio_y, termino_x, termino_y, cuadrante, subcuadrante):
        self.nombre = nombre
        self.inicio_x = inicio_x
        self.inicio_y = inicio_y
        self.termino_x = termino_x
        self.termino_y = termino_y
        self.cuadrante = cuadrante
        self.subcuadrante = subcuadrante
        self.basura_actual = 0
        self.borde = False
        self.recogida_hoy = 0 # Variable que se setea en 1 si es que un camión pasa RECOGIENDO BASURA ese día.

    def __repr__(self):
        return self.nombre

    def __str__(self):
        return "La calle '{}' que comienza en [{},{}] y termina en [{},{}] pertenece al cuadrante {} y subcuadrante {} tiene actualmente {} kilogramos de basura.".format(self.nombre, self.inicio_x, self.inicio_y, self.termino_x, self.termino_y, self.cuadrante, self.subcuadrante, self.basura_actual)

    def distancia_origen_inicio(self):
        return (100 * self.inicio_x) + (100 * self.inicio_y)

    def distancia_origen_termino(self):
        return self.distancia_origen_inicio() + 100


class Camion_chico:
    contador = 1
    def __init__(self,cuadrante, calles_cuadrante_a_recolectar):
        self.id = Camion_chico.contador
        Camion_chico.contador += 1
        self.cuadrante = cuadrante
        self.capacidad_maxima = 180
        self.basura_actual = 0
        self.tiempo_recoleccion = 0
        self.tiempo_desplazamiento = 0
        self.tiempo_total = 0
        self.tiempo_siguiente_evento = 0
        self.velocidad_desplazamiento_recoleccion = 15/3.6
        self.velocidad_desplazamiento_sinrecolectar = 50/3.6
        self.tiempo_de_espera_vaciado = 0
        self.cantidad_de_vaciados = 0 #cada vez que el camión bote su basura
        self.status = "STANDBY" #"fuera de servicio", "standby", "trasladandose", "recolectando", "vaciando", "lleno"
        self.calles_recolectadas = 0
        self.calles_transportadas = 0
        self.calles_por_recolectar = len(calles_cuadrante_a_recolectar)
        self.calles_a_recolectar = calles_cuadrante_a_recolectar
        self.ruteo_recoleccion = list()
        self.calle_actual = None

    def __str__(self):
        return "El camión chico '{}' debe recolectar {} calles en el cuadrente {}".format(self.id, self.calles_por_recolectar, self.cuadrante)

    def inicio_dia(self): #INCOMPLETA
        self.calles_a_recolectar = self.ruteo_recoleccion

    def recoleccion(self):
        calle = self.calles_a_recolectar.pop(0)
        aux = self.basura_actual
        aux2 = calle.basura_actual
        self.basura_actual += calle.basura_actual
        calle.basura_actual = 0
        self.calles_recolectadas += 1
        if self.basura_actual >= self.capacidad_maxima:
            calle.basura_actual = self.basura_actual - aux
            self.basura_actual = self.capacidad_maxima
            self.calles_recolectadas -= 1
            #print("El camión chico {} se llenó en la calle '{}'".format(self.id, calle.nombre))
            self.calle_actual = calle
            return True
        elif aux2 != 0:
            #print("El camión chico {} recolectó {} kg de basura en la calle '{}'".format(self.id, aux2, calle.nombre)) 
            return False 

    def tiempo_en_recolectar(self, tiempo_simulacion):
        self.status = "RECOLECTANDO"
        tiempo = tiempo_simulacion
        for calle in self.calles_a_recolectar:
            tiempo += 100/self.velocidad_desplazamiento_recoleccion 
            if self.recoleccion():
                self.tiempo_siguiente_evento = tiempo
                return self.tiempo_siguiente_evento
                

    def minimo_cuadrante(self): #DETERMINA EL PUNTO MÍNIMO DEL CUADRANTE
        minimo_x = infinito
        minimo_y = infinito        
        for calle in self.calles_a_recolectar:
            if calle.inicio_x < minimo_x:
                minimo_x = calle.inicio_x
            if calle.inicio_y < minimo_y:
                minimo_y = calle.inicio_y
        return [minimo_x, minimo_y]

    def definir_orden_recoleccion(self):  ## debemos crear la función de ruteo para generar una LISTA ORDENADA, que defina el movimiento a
        xmin = 62
        ymin = 62
        xmax = -1
        ymax = -1
        subiendo = True
        orden = []
        for calle in self.calles_a_recolectar:
            ## determinamos la coordenada minima y máxima dentro del cuadrante.
            if calle.inicio_x < xmin:
                xmin = calle.inicio_x
            if calle.inicio_y < ymin:
                ymin = calle.inicio_y
            if calle.termino_x > xmax:
                xmax = calle.termino_x
            if calle.termino_y > ymax:
                ymax = calle.termino_y
        yactual = ymin
        for xactual in range(xmin, xmax + 1):  ## Determinamos el orden de todas las calles verticales.
            while (True):
                for calle in self.calles_a_recolectar:
                    if subiendo:
                        if calle.inicio_x == xactual and calle.inicio_y == yactual and calle.termino_x == xactual \
                                and calle.termino_y == yactual + 1:
                            orden.append(calle)
                            #print("PUNTO S  ({}, {})".format(xactual, yactual))
                            self.calles_a_recolectar.remove(calle)
                            if yactual + 1 >= ymax:
                                calle.borde = True
                    else:
                        if calle.inicio_x == xactual and calle.inicio_y == yactual - 1 and calle.termino_x == xactual \
                                and calle.termino_y == yactual:
                            orden.append(calle)
                            #print("PUNTO SN ({}, {})".format(xactual, yactual))
                            self.calles_a_recolectar.remove(calle)
                            if yactual - 1 == ymin:
                                calle.borde = True
                if subiendo:
                    yactual += 1
                    if yactual >= ymax:
                        subiendo = False
                        break
                else:
                    yactual -= 1
                    if yactual == ymin:
                        subiendo = True
                        break
        xactual = xmax
        devolviendo = True

        for yactual in range(ymax, ymin - 1, -1):  ## Determinamos el orden de todas las calles horizontales.
            while (True):
                for calle in self.calles_a_recolectar:
                    if devolviendo:
                        if calle.inicio_x == xactual - 1 and calle.inicio_y == yactual and calle.termino_x == xactual and calle.termino_y == yactual:
                            orden.append(calle)
                            #print("PUNTO D  ({}, {})".format(xactual, yactual))
                            self.calles_a_recolectar.remove(calle)
                            if xactual - 1 <= xmin:
                                calle.borde = True
                    else:
                        if calle.inicio_x == xactual and calle.inicio_y == yactual and calle.termino_x == xactual + 1 and calle.termino_y == yactual:
                            orden.append(calle)
                            #print("PUNTO DN ({}, {})".format(xactual, yactual))
                            self.calles_a_recolectar.remove(calle)
                            if xactual + 1 >= xmax:
                                calle.borde = True
                # print("PUNTO ({} , {})".format(xactual,yactual))
                if devolviendo == True:
                    xactual -= 1
                    if xactual <= xmin:
                        devolviendo = False
                        break
                else:
                    xactual += 1
                    if xactual >= xmax:
                        devolviendo = True
                        break
        #print(orden)
        self.ruteo_recoleccion = orden
        self.calles_a_recolectar = orden
        #print("La cantidad de calles ordenadas es {}".format(len(self.calles_a_recolectar)))
        #print("La cantidad de calles iniciales es {}".format(self.calles_por_recolectar))

    def tiempo_traslado_acopio(self, tiempo_simulacion):
        tiempo = tiempo_simulacion
        self.status = "YENDO A VACIAR"
        self.tiempo_siguiente_evento = tiempo + self.tiempo_desde_origen((self.calle_actual.termino_x, self.calle_actual.termino_y))
        return self.tiempo_siguiente_evento
    
    def tiempo_traslado_cuadrante(self, tiempo_simulacion):
        tiempo = tiempo_simulacion
        self.status = "YENDO A CUADRANTE"
        self.tiempo_siguiente_evento = tiempo + self.tiempo_desde_origen((self.calles_a_recolectar[0].inicio_x, self.calles_a_recolectar[0].inicio_y))
        return self.tiempo_siguiente_evento

    def tiempo_desde_origen(self, coordenadas):
        x = coordenadas[1]
        y = coordenadas[0]
        return ((100 * x) + (100 * y))/self.velocidad_desplazamiento_sinrecolectar

class Camion_grande:

    def __init__(self):
        self.capacidad_maxima = 1600
        self.basura_actual = 0
        self.velocidad_desplazamiento_sinrecolectar = 90
        self.tiempo_sin_camiones = 0
        self.tiempo_vaciando = 0
        self.tiempo_vaciado_centro_acopio = 30 * 60
        self.vaciando = 0  # seteamos en 1 si es que un camión chico está vaciandose.
        self.status = "CENTRO DE ACOPIO" #'CENTRO DE ACOPIO', 'VACIADO'
        self.cola_vaciado = [] #cola para definir orden camiones.
        self.tiempo_siguiente_evento = infinito

    def ida_vaciado(self, tiempo_simulacion):  ##cada vez que el camión se llena ejecutamos el movimiento
        tiempo = tiempo_simulacion
        self.status = "VACIADO"
        tiempo += 2 * (30/self.velocidad_desplazamiento_sinrecolectar)*3600
        tiempo += self.tiempo_vaciado_centro_acopio
        self.tiempo_siguiente_evento = tiempo
        return self.tiempo_siguiente_evento
    
    def descarga_camion_chico(self, tiempo_simulacion):
        if len(self.cola_vaciado) != 0:
            camion = self.cola_vaciado.pop(0)
            self.basura_actual += camion.basura_actual
            camion.basura_actual = 0
            camion.status = "VACIANDO"
            camion.tiempo_siguiente_evento = tiempo_simulacion + 20 * 60
            self.tiempo_siguiente_evento = camion.tiempo_siguiente_evento
            if self.basura_actual >= self.capacidad_maxima:
                self.ida_vaciado(tiempo_simulacion)
        else:
            self.tiempo_siguiente_evento = infinito
            

            




