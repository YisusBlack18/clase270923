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


if __name__ == "__main__":
    texto = input("Ingresa el texto a encriptar: ")
    texto_encriptado = encriptar(texto)
    print(texto_encriptado)