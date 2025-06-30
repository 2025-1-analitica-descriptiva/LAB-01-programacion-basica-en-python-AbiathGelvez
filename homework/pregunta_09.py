"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    conteo_claves = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            columna5 = partes[4].split(",")
            for par in columna5:
                clave = par.split(":")[0]
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1

    return dict(sorted(conteo_claves.items()))
