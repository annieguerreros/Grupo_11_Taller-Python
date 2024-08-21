# -*- coding: utf-8 -*-
"""GRUPO_11_TAREA 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tcK8D0iOgbR2lQu7YC0U7Ftu81y-f8fP
"""

import pandas as pd

data_ciudades = {
    'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
    'Habitantes': [1047996, 1000169, 92331, 428450, 305717, 484475, 441649, 385098, 294395, 283734],
    'Area_km2': [2672.28, 1545.77, 1487.7, 116.5, 279.89, 6217.26, 368.9, 109.19, 59.4, 483.44],
    'Altitud_m': [154, 2325, 34, 3399, 29, 29, 106, 3271, 562, 156],
    'Densidad_poblacion_por_km2': [3924, 64.8, 62.1, 3673, 1091.6, 77.9, 1196, 3528.6, 4966, 587.2]}


nfos = pd.DataFrame(data_ciudades)
nfos

data_ciudades_2 = {
    'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
    'Gentilicio': ['Limeño', 'Arequipeño', 'Trujillano', 'Cusqueño', 'Chiclayano', 'Piurano', 'Iquiteño', 'Huancaino', 'Tacneño', 'Pucallpino'],
    'Provincia': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Maynas', 'Huancayo', 'Tacna', 'Coronel Portillo'],
    'Region': ['Lima', 'Arequipa', 'La Libertad', 'Cusco', 'Lambayeque', 'Piura', 'Loreto', 'Junín', 'Tacna', 'Ucayali']
}


nombres = pd.DataFrame(data_ciudades_2)

# Mostrar
nombres

cuadro_completo = pd.merge(nfos, nombres, on='Ciudad', how='inner')

# Mostramos
cuadro_completo

# Estadísticas descriptivas del DataFrame
descripcion = cuadro_completo.describe()

# Summary
print(descripcion)

min_densidad = cuadro_completo['Densidad_poblacion_por_km2'].min()
max_densidad = cuadro_completo['Densidad_poblacion_por_km2'].max()

ciudad_min_densidad = cuadro_completo[cuadro_completo['Densidad_poblacion_por_km2'] == min_densidad]['Ciudad'].values[0]
ciudad_max_densidad = cuadro_completo[cuadro_completo['Densidad_poblacion_por_km2'] == max_densidad]['Ciudad'].values[0]

# Results
print(f"La mínima densidad poblacional es {min_densidad} y corresponde a la ciudad de {ciudad_min_densidad}.")
print(f"La máxima densidad poblacional es {max_densidad} y corresponde a la ciudad de {ciudad_max_densidad}.")

import matplotlib.pyplot as plt

cuadro_completo = pd.merge(nfos, nombres, on='Ciudad', how='inner')

plt.figure(figsize=(12, 6))
plt.bar(cuadro_completo['Ciudad'], cuadro_completo['Habitantes'], color='skyblue')
plt.xlabel('Ciudad')
plt.ylabel('Cantidad de Habitantes')
plt.title('Cantidad de Habitantes en Cada Ciudad')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar
plt.show()

#GRAFICO DISPERSION
plt.figure(figsize=(10, 6))
plt.scatter(cuadro_completo['Altitud_m'], cuadro_completo['Habitantes'], color='coral', edgecolor='black')
plt.xlabel('Altitud (m)')
plt.ylabel('Número de Habitantes')
plt.title('Gráfico de Dispersión entre Altitud y Número de Habitantes')
plt.grid(True)


plt.show()

