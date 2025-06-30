"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12():
    suma_por_letra = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            letra = partes[0]
            pares = partes[4].split(",")
            suma = sum(int(par.split(":")[1]) for par in pares)

            if letra in suma_por_letra:
                suma_por_letra[letra] += suma
            else:
                suma_por_letra[letra] = suma

    return dict(sorted(suma_por_letra.items()))
