"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    valores_por_clave = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            columna5 = partes[4].split(",")
            for par in columna5:
                clave, valor = par.split(":")
                valor = int(valor)
                if clave in valores_por_clave:
                    valores_por_clave[clave].append(valor)
                else:
                    valores_por_clave[clave] = [valor]

    resultado = []
    for clave in sorted(valores_por_clave.keys()):
        minimo = min(valores_por_clave[clave])
        maximo = max(valores_por_clave[clave])
        resultado.append((clave, minimo, maximo))

    return resultado

