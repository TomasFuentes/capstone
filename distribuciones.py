### GRUPO 7 ###
### Taller de Investigación Operativa ###

import warnings
import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels as sm
import matplotlib
import matplotlib.pyplot as plt
import json

matplotlib.rcParams['figure.figsize'] = (16.0, 12.0)
matplotlib.style.use('ggplot')


# Crear modelo desde datos
def best_fit_distribution(data, bins=200, ax=None):
    """Modelar los datos encontrando una distribución que se ajuste"""
    # Obtener el histograma de los datos originales
    y, x = np.histogram(data, bins=bins, density=True)
    x = (x + np.roll(x, -1))[:-1] / 2.0

    # Distribuciones que se chequean
    DISTRIBUTIONS = [
        st.alpha, st.anglit, st.arcsine, st.beta, st.betaprime, st.bradford, st.burr, st.cauchy, st.chi, st.chi2,
        st.cosine, st.dgamma, st.dweibull, st.erlang, st.expon, st.exponnorm, st.exponweib, st.exponpow, st.f, st.fatiguelife,
        st.fisk, st.foldcauchy, st.foldnorm, st.frechet_r, st.frechet_l, st.genlogistic, st.genpareto, st.gennorm, st.genexpon,
        st.genextreme, st.gausshyper, st.gamma, st.gengamma, st.genhalflogistic, st.gilbrat, st.gompertz, st.gumbel_r,
        st.gumbel_l, st.halfcauchy, st.halflogistic, st.halfnorm, st.halfgennorm, st.hypsecant, st.invgamma, st.invgauss,
        st.invweibull, st.johnsonsb, st.johnsonsu, st.ksone, st.kstwobign, st.laplace, st.levy, st.levy_l,
        st.ncf, st.nct, st.norm, st.pareto, st.pearson3, st.powerlaw, st.powerlognorm, st.powernorm, st.rdist, st.reciprocal,
        st.rayleigh, st.rice, st.recipinvgauss, st.semicircular, st.t, st.triang, st.truncexpon, st.truncnorm,
        st.tukeylambda, st.uniform, st.vonmises, st.vonmises_line, st.wald, st.weibull_min, st.weibull_max, st.wrapcauchy,
        st.logistic, st.loggamma, st.lognorm]

    # Mejores sostenedores
    best_distribution = st.norm
    best_params = (0.0, 1.0)
    best_sse = np.inf

    # Estimación de los diferentes parámetros de los datos.
    for distribution in DISTRIBUTIONS:

        # Intentar calzar la distribución
        try:
            # Ignorar las advertencias para las distribuciones que no se pueden calzar.
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore')

                # Calzar la distribución a los datos.
                params = distribution.fit(data)

                # Separación de los parámetros
                arg = params[:-2]
                loc = params[-2]
                scale = params[-1]

                # Calcular la función de probabilidad calzada y el error con el modelo.
                pdf = distribution.pdf(x, loc=loc, scale=scale, *arg)
                sse = np.sum(np.power(y - pdf, 2.0))

                # Agregar los ejes a la dsitribución
                try:
                    if ax:
                        pd.Series(pdf, x).plot(ax=ax)
                except Exception:
                    pass

                # Identificar si esta distribución es la mejor
                if best_sse > sse > 0:
                    best_distribution = distribution
                    best_params = params
                    best_sse = sse

        except Exception:
            pass

    return (best_distribution.name, best_params)


def make_pdf(dist, params, size=10000):
    """Encontrar la función de densidad"""

    # Separación de los parámetros
    arg = params[:-2]
    loc = params[-2]
    scale = params[-1]

    # Obtener los puntos de inicio y término
    start = dist.ppf(0.01, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.01, loc=loc, scale=scale)
    end = dist.ppf(0.99, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.99, loc=loc, scale=scale)

    # Construir la función de densidad de probabilidad y convertirla a Series de Pandas
    x = np.linspace(start, end, size)
    y = dist.pdf(x, loc=loc, scale=scale, *arg)
    pdf = pd.Series(y, x)

    return pdf


with open('data.txt') as json_file:
    datos2 = json.load(json_file)

# Cargar los datos desde la hoja de statsmodels
basura_total = []
contador = 0

for nodo in datos2:
    contador = 0
    while contador <= 27:
        basura_total.append([])
        basura_total[contador].append(datos2[nodo]["datos_historicos"][contador])
        contador += 1


data = pd.Series(basura_total[20])

# Ploteo para comparación
plt.figure(figsize=(12, 8))
ax = data.plot(kind='hist', bins=10, density=True, alpha=0.5)  # color=plt.rcParams['axes.color_cycle'][1])

# Guardar los límites del plot
dataYLim = ax.get_ylim()

# Encontrar la mejor distribución
best_fit_name, best_fit_params = best_fit_distribution(data, 200, ax)
best_dist = getattr(st, best_fit_name)

# Actualizar los plots
ax.set_ylim(dataYLim)
ax.set_title(u'Frecuencia de Basura en la Comuna.\n Todas las distribuciones acomodadas')
ax.set_xlabel(u'Basura (Kg)')
ax.set_ylabel('Frecuencia')

# Obtener la función de densidad con los mejores parámetros.
pdf = make_pdf(best_dist, best_fit_params)

# Display
plt.figure(figsize=(12, 8))
ax = pdf.plot(lw=2, label='PDF', legend=True)
data.plot(kind='hist', bins=10, density=True, alpha=0.5, label='Data', legend=True, ax=ax)

param_names = (best_dist.shapes + ', loc, scale').split(', ') if best_dist.shapes else ['loc', 'scale']
param_str = ', '.join(['{}={:0.2f}'.format(k, v) for k, v in zip(param_names, best_fit_params)])
dist_str = '{}({})'.format(best_fit_name, param_str)

ax.set_title(
    u'Frecuencia de Basura en la Comuna con su mejor Distribución \n' + dist_str)
ax.set_xlabel(u'Basura (Kg)')
ax.set_ylabel('Frecuencia')
plt.show()
