#!/usr/bin/python3
import pyperclip

'''
    Programa que tira todas quebras de linhas de uma string 
copiada para o clipboard. Muito útil para textos grandes
copiados diretamente de pdfs.
'''

text = pyperclip.paste().split('\n')
print(text)
text = ' '.join(text)

pyperclip.copy(text)