# -*- coding: utf-8 -*-
"""GRUPO_11_Tarea3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HS2sNg43-FAq8gZVGlxTCcMW0Z4zNelS

## TAREA **3**

## **Ejercicio 1**

> Utilizando scipy. stats, crea un programa que modele la probabilidad de obtener un
número específico de éxitos en una serie de lanzamientos de una moneda sin trucos
(probabilidad de éxito p = 0. 5). Genera la probabilidad de obtener exactamente 7 caras
en 10 lanzamientos
"""

import scipy.stats as stats
# Parámetros
n = 10  # Número total de lanzamientos
p = 0.5  # Probabilidad de éxito en cada lanzamiento
k = 7  # Número de éxitos deseados

# Calcular la probabilidad usando la distribución binomial
probabilidad = stats.binom.pmf(k, n, p)

print(f"La probabilidad de obtener exactamente {k} éxitos en {n} lanzamientos es: {probabilidad:.4f}")

"""## **Ejercicio 2**

> Calcula la probabilidad acumulada de obtener 7 o menos caras en 10 lanzamientos


"""

import scipy.stats as stats
# Parámetros
n = 10  # Número total de lanzamientos
p = 0.5  # Probabilidad de éxito en cada lanzamiento
k = 7  # Número de éxitos deseados

#Distribución binomial
probabilidad_acumulada = stats.binom.cdf(k, n, p)

print(f"La probabilidad acumulada de obtener {k} o menos éxitos en {n} lanzamientos es: {probabilidad_acumulada:.4f}")

"""## **Ejercicio 3**

> Grafica la distribución binomial completa para los 10 lanzamientos, mostrando la probabilidad de obtener desde 0 hasta 10 caras.


"""

import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Parámetros
n = 10  # Número total de lanzamientos
p = 0.5  # Probabilidad de éxito en cada lanzamiento

# Valores posibles de éxitos (desde 0 hasta n)
k_values = np.arange(0, n+1)

# Calcular las probabilidades usando la distribución binomial
probabilidades = stats.binom.pmf(k_values, n, p)

# Graficar la distribución
plt.bar(k_values, probabilidades, color='skyblue', edgecolor='black')
plt.xticks(k_values)
plt.xlabel('Número de caras (éxitos)')
plt.ylabel('Probabilidad')
plt.title('Distribución Binomial para 10 lanzamientos de una moneda sin trucos')
plt.show()

"""## **Ejercicio 4**

> Ahora la moneda tiene mayor probabilidad de caer en cara (probabilidad de éxito 𝒑=𝟎.𝟖). ¿Cómo cambian los resultados? Vuelve a realizar los ejercicios I, II y III.


"""

import scipy.stats as stats
# Definir parámetros
n = 10  # Número total de lanzamientos
p = 0.8  # Probabilidad de éxito en cada lanzamiento
k = 7  # Número de éxitos deseados

probabilidad = stats.binom.pmf(k, n, p)

print(f"La probabilidad de obtener exactamente {k} éxitos en {n} lanzamientos es: {probabilidad:.4f}")

import scipy.stats as stats
# Definir parámetros
n = 10
p = 0.8
k = 7

probabilidad_acumulada = stats.binom.cdf(k, n, p)

print(f"La probabilidad acumulada de obtener {k} o menos éxitos en {n} lanzamientos es: {probabilidad_acumulada:.4f}")

import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Definir parámetros
n = 10
p = 0.8

k_values = np.arange(0, n+1)

probabilidades = stats.binom.pmf(k_values, n, p)

# Graficar la distribución binomial completa para 10 lanzamientos con el nuevo p
plt.bar(k_values, probabilidades, color='skyblue', edgecolor='black')
plt.xticks(k_values)
plt.xlabel('Número de caras (éxitos)')
plt.ylabel('Probabilidad')
plt.title('Distribución Binomial para 10 lanzamientos de una moneda sin trucos')
plt.show()

"""## **Ejercicio 5**

> Utilizando 𝒔𝒄𝒊𝒑𝒚.𝒔𝒕𝒂𝒕𝒔, realiza un análisis de una distribución normal con una media de 0 y desviación estándar de 1. Genera un conjunto de datos aleatorios con 1000 muestras a partir de esta distribución.


"""

import numpy as np

mean = 0
std_dev = 1
samples = np.random.normal(mean, std_dev, 1000)

"""## **Ejercicio 6**

> Calcular media, desviación estándar y mediana de los datos generados


"""

calculated_mean = np.mean(samples)
calculated_std_dev = np.std(samples)
calculated_median = np.median(samples)

"""### **Ejercicio 7**

>  Graficar histograma de los datos y superponer la curva de distribución normal teórica


"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, binom

# Generar muestra de datos
mean = 0
std_dev = 1
samples = np.random.normal(mean, std_dev, 1000)

# Crear histograma
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=30, density=True, alpha=0.6, color='gray')

# Superposición de la curva teórica de la distribución normal
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)  # Distribución normal teórica
plt.plot(x, p, 'k', linewidth=2)
title = "Histograma de Datos y Curva de Distribución Normal (media=0, std_dev=1)"
plt.title(title)
plt.xlabel("Valor")
plt.ylabel("Densidad de Probabilidad")
plt.show()

# Calcular probabilidades binomiales
n = 10  # Número de ensayos (lanzamientos de moneda)
p1 = 0.5  # Probabilidad de éxito (moneda justa)
p2 = 0.8  # Probabilidad de éxito con sesgo

# Probabilidades para p = 0.5 (moneda justa)
prob_exact_7_heads = binom.pmf(7, n, p1)  # Probabilidad de exactamente 7 caras
prob_7_or_less_heads = binom.cdf(7, n, p1)  # Probabilidad acumulada de 7 o menos caras

# Probabilidades para p = 0.8 (moneda sesgada)
prob_exact_7_heads_new = binom.pmf(7, n, p2)  # Probabilidad de exactamente 7 caras
prob_7_or_less_heads_new = binom.cdf(7, n, p2)  # Probabilidad acumulada de 7 o menos caras

# Calcular estadísticas sobre los datos generados
calculated_mean = np.mean(samples)  # Media de los datos generados
calculated_std_dev = np.std(samples)  # Desviación estándar de los datos generados
calculated_median = np.median(samples)  # Mediana de los datos generados

# Imprimir los resultados
print("Probabilidad de obtener exactamente 7 caras (p=0.5):", prob_exact_7_heads)
print("Probabilidad acumulada de obtener 7 o menos caras (p=0.5):", prob_7_or_less_heads)
print("Probabilidad de obtener exactamente 7 caras (p=0.8):", prob_exact_7_heads_new)
print("Probabilidad acumulada de obtener 7 o menos caras (p=0.8):", prob_7_or_less_heads_new)
print("Media calculada:", calculated_mean)
print("Desviación estándar calculada:", calculated_std_dev)
print("Mediana calculada:", calculated_median)

"""## **Ejercicio 8**

> Calcula la probabilidad de que un valor caiga dentro del rango de -1 a 1 (una desviación estándar de la media).


"""

from scipy.stats import norm

# Parámetros de la distribución normal
mean = 0
std_dev = 1

# Calcular la probabilidad de estar dentro de una desviación estándar de la media (rango de -1 a 1)
prob_within_1_std_dev = norm.cdf(1, mean, std_dev) - norm.cdf(-1, mean, std_dev)

print("Probabilidad de que un valor caiga dentro de una desviación estándar (de -1 a 1):", prob_within_1_std_dev)