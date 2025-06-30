"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    agrupacion = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            letra = partes[0]
            numero = int(partes[1])


            if numero not in agrupacion:
                agrupacion[numero] = set()
            agrupacion[numero].add(letra)

    resultado = []
    for numero in sorted(agrupacion.keys()):
        letras_ordenadas = sorted(agrupacion[numero])
        resultado.append((numero, letras_ordenadas))

    return resultado
