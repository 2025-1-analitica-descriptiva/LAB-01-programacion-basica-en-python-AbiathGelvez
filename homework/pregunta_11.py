"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    suma_por_letra = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            valor = int(partes[1])
            letras = partes[3].split(",")
            for letra in letras:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor
                else:
                    suma_por_letra[letra] = valor

    return dict(sorted(suma_por_letra.items()))
