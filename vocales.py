def contar_vocales(palabra):
    vocales = ("a", "e", "i", "o", "u")
    resultado = {}
    for letra in palabra:
        if letra in vocales:
            # La letra es vocal
            if letra in resultado.keys():
                # Sumar valor a diccionario ya existente
                resultado[letra] += 1
            else:
                # Agregar letra por primera vez
                resultado[letra] = 1

    return resultado