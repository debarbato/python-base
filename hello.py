#! /usr/local/bin/python3
#Este programa imprime Hello World
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

obs: Use o comando env | grep LANG para saber a lingua configurada do seu ambiente.

Como usar:

Tenha a vairavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
#Dunder > 2 underlines
__version__ = "0.0.1"
__author__ = "David Barbato"
__license__ = "Unlicense"

#module os serve para ler a variavel ambiente
import os

current_language = os.getenv("LANG", "en_US")[:5] #en_US é usado caso nao exista a variavelde ambiete LANG

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"  

print(msg)
