#este programa encripta un texto por desplazamiento
# -*- coding: utf-8 -*-

def encriptar(texto):
    texto_encriptado = ""
    for letra in texto:
        if letra == " ":
            texto_encriptado += " "
        else:
            texto_encriptado += chr(ord(letra) + 3)
    return texto_encriptado

def desencriptar(texto):
    texto_desencriptado = ""
    for letra in texto:
        if letra == " ":
            texto_desencriptado += " "
        else:
            texto_desencriptado += chr(ord(letra) - 3)
    return texto_desencriptado


if __name__ == "__main__":
    print("Encriptador de texto Oullea")
    texto = input("Ingresa el texto a encriptar: ")
    # arreglos-caracteristicas
    texto_encriptado = encriptar(texto)
    texto_desencriptado = desencriptar(texto_encriptado)
    # caracteristicas-nuevas
    print(texto_encriptado)
