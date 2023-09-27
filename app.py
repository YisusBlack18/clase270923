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


