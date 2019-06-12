### GRUPO 7 ###
### Taller de Investigación Operativa ###

import warnings
import numpy as np
import pandas as pd
import json

with open('data.txt') as json_file:
    datos = json.load(json_file)
    
for key in datos:
    datos[key].pop("xcoord", None)
    datos[key].pop("ycoord", None)
    datos[key].pop("datos_historicos", None)
    #Cuadrante 1
    if datos[key]["termina"][1] <= 22 and datos[key]["termina"][0] <= 15:
        datos[key]["cuadrante"] = 1
    #Cuadrante 2
    if datos[key]["termina"][1] <= 22 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][0] >= 15:
            datos[key]["cuadrante"] = 2
    #Cuadrante 3
    if datos[key]["termina"][1] <= 33 and datos[key]["termina"][0] <= 23:
        if datos[key]["comienza"][1] >= 22:
            datos[key]["cuadrante"] = 3
    #Cuadrante 4
    if datos[key]["termina"][1] <= 19 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 27:
            datos[key]["cuadrante"] = 4
    #Cuadrante 5
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][1] >= 19 and datos[key]["comienza"][0] >= 27:
            datos[key]["cuadrante"] = 5
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][1] >= 22 and datos[key]["comienza"][0] >= 23:
            datos[key]["cuadrante"] = 5
    #Cuadrante 6
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 20:
        if datos[key]["comienza"][1] >= 33:
            datos[key]["cuadrante"] = 6
    #Cuadrante 7
    if datos[key]["termina"][1] <= 12 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 36:
            datos[key]["cuadrante"] = 7
    #Cuadrante 8
    if datos[key]["termina"][1] <= 24 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 36 and datos[key]["comienza"][1] >= 12:
            datos[key]["cuadrante"] = 8
    #Cuadrante 9
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 18:
        if datos[key]["comienza"][0] >= 9 and datos[key]["comienza"][1] >= 43:
            datos[key]["cuadrante"] = 9
    #Cuadrante 10
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 9:
        if datos[key]["comienza"][1] >= 43:
            datos[key]["cuadrante"] = 10
    #Cuadrante 11
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 36 and datos[key]["comienza"][1] >= 24:
            datos[key]["cuadrante"] = 11
    #Cuadrante 12
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 35 and datos[key]["comienza"][1] >= 34:
            datos[key]["cuadrante"] = 12
    #Cuadrante 13
    if datos[key]["termina"][1] <= 44 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 35 and datos[key]["comienza"][1] >= 43:
            datos[key]["cuadrante"] = 13
    if datos[key]["termina"][1] <= 44 and datos[key]["termina"][0] <= 35:
        if datos[key]["comienza"][0] >= 23 and datos[key]["comienza"][1] >= 34:
            datos[key]["cuadrante"] = 13
    if datos[key]["termina"][1] <= 44 and datos[key]["termina"][0] <= 23:
        if datos[key]["comienza"][0] >= 20 and datos[key]["comienza"][1] >= 33:
            datos[key]["cuadrante"] = 13
    #Cuadrante 14
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][1] >= 44 and datos[key]["comienza"][0] >= 27:
            datos[key]["cuadrante"] = 14
    #Cuadrante 15
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][1] >= 44 and datos[key]["comienza"][0] >= 20:
            datos[key]["cuadrante"] = 15
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 20:
        if datos[key]["comienza"][1] >= 43 and datos[key]["comienza"][0] >= 18:
            datos[key]["cuadrante"] = 15
    #Cuadrante 16
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 43:
        if datos[key]["comienza"][1] >= 43 and datos[key]["comienza"][0] >= 36:
            datos[key]["cuadrante"] = 16
    #Cuadrante 17
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][1] >= 43 and datos[key]["comienza"][0] >= 43:
            datos[key]["cuadrante"] = 17

    #Cuadrante 1
    if datos[key]["termina"][1] <= 8 and datos[key]["termina"][0] <= 15:
        datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 15 and datos[key]["termina"][0] <= 15:
        if datos[key]["comienza"][1] >= 8:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 22 and datos[key]["termina"][0] <= 15:
        if datos[key]["comienza"][1] >= 15:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 2
    if datos[key]["termina"][1] <= 8 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][0] >= 15:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 15 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][0] >= 15 and datos[key]["comienza"][1] >= 8:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 22 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][0] >= 15 and datos[key]["comienza"][1] >= 15:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 3
    if datos[key]["termina"][1] <= 33 and datos[key]["termina"][0] <= 7:
        if datos[key]["comienza"][1] >= 22:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 33 and datos[key]["termina"][0] <= 15:
        if datos[key]["comienza"][1] >= 22 and datos[key]["comienza"][0] >= 7:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 33 and datos[key]["termina"][0] <= 23:
        if datos[key]["comienza"][1] >= 22 and datos[key]["comienza"][0] >= 15:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 4
    if datos[key]["termina"][1] <= 7 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 27:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 13 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 27 and datos[key]["comienza"][1] >= 7:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 19 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 27 and datos[key]["comienza"][1] >= 13:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 5
    if datos[key]["termina"][1] <= 24 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][1] >= 19 and datos[key]["comienza"][0] >= 27:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 24 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][1] >= 22 and datos[key]["comienza"][0] >= 23:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 29 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][1] >= 24 and datos[key]["comienza"][0] >= 23:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][1] >= 29 and datos[key]["comienza"][0] >= 23:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 6
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 20:
        if datos[key]["comienza"][1] >= 33 and datos[key]["comienza"][0] >= 13:
            datos[key]["subcuadrante"] = 3
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 13:
        if datos[key]["comienza"][1] >= 33 and datos[key]["comienza"][0] >= 6:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 6:
        if datos[key]["comienza"][1] >= 33 and datos[key]["comienza"][0] >= 0:
            datos[key]["subcuadrante"] = 1
    #Cuadrante 7
    if datos[key]["termina"][1] <= 12 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 45:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 12 and datos[key]["termina"][0] <= 45:
        if datos[key]["comienza"][0] >= 40:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 12 and datos[key]["termina"][0] <= 40:
        if datos[key]["comienza"][0] >= 36:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 8
    if datos[key]["termina"][1] <= 24 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 45 and datos[key]["comienza"][1] >= 12:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 24 and datos[key]["termina"][0] <= 45:
        if datos[key]["comienza"][0] >= 40 and datos[key]["comienza"][1] >= 12:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 24 and datos[key]["termina"][0] <= 40:
        if datos[key]["comienza"][0] >= 36 and datos[key]["comienza"][1] >= 12:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 9
    if datos[key]["termina"][1] <= 49 and datos[key]["termina"][0] <= 18:
        if datos[key]["comienza"][0] >= 9 and datos[key]["comienza"][1] >= 43:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 55 and datos[key]["termina"][0] <= 18:
        if datos[key]["comienza"][0] >= 9 and datos[key]["comienza"][1] >= 49:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 18:
        if datos[key]["comienza"][0] >= 9 and datos[key]["comienza"][1] >= 55:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 10
    if datos[key]["termina"][1] <= 49 and datos[key]["termina"][0] <= 9:
        if datos[key]["comienza"][1] >= 43:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 55 and datos[key]["termina"][0] <= 9:
        if datos[key]["comienza"][1] >= 49:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 9:
        if datos[key]["comienza"][1] >= 55:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 11
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 45 and datos[key]["comienza"][1] >= 24:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 45:
        if datos[key]["comienza"][0] >= 40 and datos[key]["comienza"][1] >= 24:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 40:
        if datos[key]["comienza"][0] >= 36 and datos[key]["comienza"][1] >= 24:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 12
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 45 and datos[key]["comienza"][1] >= 34:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 45:
        if datos[key]["comienza"][0] >= 40 and datos[key]["comienza"][1] >= 34:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 43 and datos[key]["termina"][0] <= 40:
        if datos[key]["comienza"][0] >= 35 and datos[key]["comienza"][1] >= 34:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 13
    if datos[key]["termina"][1] <= 37 and datos[key]["termina"][0] <= 35:
        if datos[key]["comienza"][0] >= 20 and datos[key]["comienza"][1] >= 34:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 34 and datos[key]["termina"][0] <= 23:
        if datos[key]["comienza"][0] >= 20 and datos[key]["comienza"][1] >= 33:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 41 and datos[key]["termina"][0] <= 35:
        if datos[key]["comienza"][0] >= 20 and datos[key]["comienza"][1] >= 37:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 44 and datos[key]["termina"][0] <= 35:
        if datos[key]["comienza"][0] >= 20 and datos[key]["comienza"][1] >= 41:
            datos[key]["subcuadrante"] = 3
    if datos[key]["termina"][1] <= 44 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 35 and datos[key]["comienza"][1] >= 43:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 14
    if datos[key]["termina"][1] <= 50 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 27 and datos[key]["comienza"][1] >= 44:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 55 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 27 and datos[key]["comienza"][1] >= 50:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 36:
        if datos[key]["comienza"][0] >= 27 and datos[key]["comienza"][1] >= 55:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 15
    if datos[key]["termina"][1] <= 50 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][0] >= 18 and datos[key]["comienza"][1] >= 44:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 44 and datos[key]["termina"][0] <= 20:
        if datos[key]["comienza"][0] >= 18 and datos[key]["comienza"][1] >= 43:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 55 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][0] >= 18 and datos[key]["comienza"][1] >= 50:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 27:
        if datos[key]["comienza"][0] >= 18 and datos[key]["comienza"][1] >= 55:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 16
    if datos[key]["termina"][1] <= 49 and datos[key]["termina"][0] <= 43:
        if datos[key]["comienza"][0] >= 36 and datos[key]["comienza"][1] >= 43:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 55 and datos[key]["termina"][0] <= 43:
        if datos[key]["comienza"][0] >= 36 and datos[key]["comienza"][1] >= 49:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 43:
        if datos[key]["comienza"][0] >= 36 and datos[key]["comienza"][1] >= 55:
            datos[key]["subcuadrante"] = 3
    #Cuadrante 17
    if datos[key]["termina"][1] <= 49 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 43 and datos[key]["comienza"][1] >= 43:
            datos[key]["subcuadrante"] = 1
    if datos[key]["termina"][1] <= 55 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 43 and datos[key]["comienza"][1] >= 49:
            datos[key]["subcuadrante"] = 2
    if datos[key]["termina"][1] <= 60 and datos[key]["termina"][0] <= 50:
        if datos[key]["comienza"][0] >= 43 and datos[key]["comienza"][1] >= 55:
            datos[key]["subcuadrante"] = 3

with open('calles.txt', 'w') as outfile:
    json.dump(datos, outfile)


            
    
