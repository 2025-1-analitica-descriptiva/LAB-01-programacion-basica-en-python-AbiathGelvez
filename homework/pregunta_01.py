"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    suma = 0
    with open("data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            suma += int(partes[1])
    return suma
