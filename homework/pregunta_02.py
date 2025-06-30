"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    conteo = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            letra = linea.strip().split("\t")[0]
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1

    # Convertir a lista de tuplas y ordenar alfabéticamente por la letra
    resultado = sorted(conteo.items())
    return resultado


