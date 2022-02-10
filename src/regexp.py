#!/usr/bin/python3

#Projeto extrator de números de 
#telefone e endereços de e-mail 
#do clipboard

import pyperclip
import re
# import sys


clip = pyperclip.paste()
tel = re.compile(r'\(?([1-9]{2})\)? ?(9?\d{4} ?-?\d{4})')
email = re.compile(r'(([a-zA-Z._]{1,20}\d*@[A-zA-Z]{1,10}\.[A-zA-Z]{1,20})(.[A-zA-Z]{1,2})?)')

#método findall retorna uma lista contendo tuplas que correspondem
#aos matches da regexp com a string comparada. As tuplas contêm strings
#que correspondem a cada grupo encontrado - () -no match em questão
moTel = tel.findall(clip)
moEma = email.findall(clip)

newClip = ' '

#aqui procura se há tuplas repetidas em minha lista 
#faço isso comparando o valor da posição i atual do for 
#com os próximas que aparecem na lista até chegar ao último
#o qual não compara com nada - range(1, 1) não executa um for-
#a mesma lógica é usada aqui.
for i in range(len(moTel)):
    conf = True
    for j in range(i+1, len(moTel)):
        if moTel[i] == moTel[j]:
            conf = False

    if conf:
        newClip += moTel[i][0]+' '+moTel[i][1]+'\n'

for i in range(len(moEma)):
    conf = True
    for j in range(i+1, len(moEma)):
        if moEma[i] == moEma[j]:
            conf = False

        
    if conf:
        newClip += moEma[i][0]+'\n'


print(newClip)
pyperclip.copy(newClip)
