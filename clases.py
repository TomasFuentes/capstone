from scipy.stats import halfgennorm
import numpy as np
import matplotlib.pyplot as plt
import json


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

    def add_calle(self, calle, data):
        self.calles.append(Calle(calle, data["comienza"][1], data["comienza"][0], data["termina"][1], data["termina"][0], data["cuadrante"], data["subcuadrante"]))

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
    contador = 0
    def __init__(self,cuadrante, calles_cuadrante_a_recolectar):
        self.id = Camion_chico.contador
        Camion_chico.contador += 1
        self.cuadrante = cuadrante
        self.capacidad_maxima = 180
        self.basura_actual = 0
        self.posicion_x = 0
        self.posicion_y = 0
        self.ultima_posicion_recolectado_x = 0
        self.ultima_posicion_recolectado_y = 0
        self.tiempo_recoleccion = 0
        self.tiempo_desplazamiento = 0
        self.tiempo_total = 0
        self.velocidad_desplazamiento_recoleccion = 50
        self.velocidad_desplazamiento_sinrecolectar = 15
        self.tiempo_de_espera_vaciado = 0
        self.cantidad_de_vaciados = 0 #cada vez que el camión bote su basura
        self.a_vaciar = 0 #seteamos en 1 si es que el camión está yendo a vaciarse.
        self.vaciando = 0 #seteamos en 1 si es que el camión está vaciandose.
        self.recolectando = 0 #seteamos en 1 si es que el camión está recolectando una calle.
        self.metros_recorridos_calle = 0 # variable para llevar registo al momento de estar recolectando
        self.calles_recolectadas = 0
        self.calles_por_recolectar = len(calles_cuadrante_a_recolectar)
        self.calles_a_recolectar = calles_cuadrante_a_recolectar
        self.ruteo_recoleccion = []
        self.calle_actual = None

    def __str__(self):
        return "El camión chico '{}' debe recolectar {} calles en el cuadrente {}".format(self.id, self.calles_por_recolectar, self.cuadrante)

    def definir_orden_recoleccion(self): ## debemos crear la función de ruteo para generar una LISTA ORDENADA, que defina el movimiento a
        pass
    def ida_vaciado(self): ##cada vez que el camión se llena, es decir a_vaciar 1 nos movemos con esta funcion para optimizar el movimiento
        pass
    def vuelta_vaciado(self): ## define el ruteo para la vuelta a recolección.
        pass


class Camion_grande:

    def __init__(self):
        self.capacidad_maxima = 1600
        self.basura_actual = 0
        self.velocidad_desplazamiento_sinrecolectar = 90
        self.tiempo_sin_camiones = 0
        self.tiempo_vaciando = 0
        self.vaciando = 0  # seteamos en 1 si es que un camión chico está vaciandose.
        self.km_recorridos_a_vaciar = 0
        self.tiempo_vaciado_camion_actual = 0 # variable que va de 0 a 20mins y es para analizar el tiempo real de vaciado del camion.
        """ver si usaremos la variable de arriba para controlar el vaciado, es decir que tenemos que definir si el camión 
        grande controla el vaciado del camión chico, o si el camión chico lo controla solo"""
        self.cola_vaciado = [] #cola para definir orden camiones.

    def ida_vaciado(self):  ##cada vez que el camión se llena ejecutamos el movimiento
        pass

    def vuelta_vaciado(self):  ## define el ruteo para la vuelta a recolección.
        pass

