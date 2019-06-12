from scipy.stats import halfgennorm
import numpy as np
import matplotlib.pyplot as plt
import json

with open('data.txt') as json_file:
    data = json.load(json_file)

beta = 24.55
loc = 1.00
scale = 3.97

for calle in data:
    data[calle]["basura_actual"] = 0

contador = 0
for rango in range(3):
    for calle in data:
        data[calle]["basura_actual"] += halfgennorm.rvs(beta, loc, scale, size=1)[0]
        if rango == 2:
            if data[calle]["basura_actual"] > 12:
                contador +=1
    x = list()
    y = list()
    for calle in data:
        x.append(data[calle]["comienza"][0])
        x.append(data[calle]["termina"][0])
        x.append(calle)
        y.append(data[calle]["comienza"][1])
        y.append(data[calle]["termina"][1])
        y.append(calle)

    for i in range(0, len(x), 3):
        if data[x[i+2]]["basura_actual"] > 12:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='0')
        elif data[x[i+2]]["basura_actual"] > 11:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#260206')
        elif data[x[i+2]]["basura_actual"] > 10:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#360000')
        elif data[x[i+2]]["basura_actual"] > 9:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#400001')
        elif data[x[i+2]]["basura_actual"] > 8:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#5f0000')
        elif data[x[i+2]]["basura_actual"] > 7:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#911202')
        elif data[x[i+2]]["basura_actual"] > 6:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#ab2700')
        elif data[x[i+2]]["basura_actual"] > 5:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#d85500')
        elif data[x[i+2]]["basura_actual"] > 4:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#f97e03')
        elif data[x[i+2]]["basura_actual"] > 3:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#ffb339')
        elif data[x[i+2]]["basura_actual"] > 2:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#fcff76')
        elif data[x[i+2]]["basura_actual"] > 1:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#fffdbd')
        elif data[x[i+2]]["basura_actual"] > 0:
            plt.plot(x[i:i+2], y[i:i+2], '-', markersize=0.8, color='#fcfdf3')
    plt.show()