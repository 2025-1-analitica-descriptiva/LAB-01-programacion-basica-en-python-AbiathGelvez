"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    valores = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            letra = partes[0]
            valor = int(partes[1])

            if letra in valores:
                valores[letra].append(valor)
            else:
                valores[letra] = [valor]

    resultado = []
    for letra in sorted(valores.keys()):
        maximo = max(valores[letra])
        minimo = min(valores[letra])
        resultado.append((letra, maximo, minimo))

    return resultado
