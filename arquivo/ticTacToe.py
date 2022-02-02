def mostra_dic(dic):
    """
        Mostra o jogo (dicionario)
    """
    print('~'*10)
    print(dicio['top-l']+'|'+dicio['top-m']+'|'+dicio['top-r'])
    print('-+-+-')
    print(dicio['mid-l']+'|'+dicio['mid-m']+'|'+dicio['mid-r'])
    print('-+-+-')
    print(dicio['low-l']+'|'+dicio['low-m']+'|'+dicio['low-r'])


def confere_vencedor(dic, user):
    """
        laços de repetição que conferem se há vencedor
    """
    for i in ['top-', 'mid-', 'low-']:
        if (dic[i+'l'] and dic[i+'m'] and dic[i+'r'] != ' ') and (dic[i+'l'] == dic[i+'m'] == dic[i+'r']):
            # print(f'Jogador {user} vencedor!')
            # print(f'{dicio["top-"+j]} {dicio["mid-"+j]}, {dicio["low-"+j]}')
            print('='*3)
            print(f'Jogador {user} vencedor!')
            mostra_dic(dic)
            print('~'*10)
            return 'fecha'

    for j in ['l', 'm', 'r']:                   
        if (dicio['top-'+j] and dicio['mid-'+j] and dicio['low-'+j] != ' ') and (dicio['top-'+j] == dicio['mid-'+j] == dicio['low-'+j]):
            # print(f'Jogador {user} vencedor!')
            # print(f'{dicio["top-"+j]} {dicio["mid-"+j]}, {dicio["low-"+j]}')
            print('-'*3)
            print(f'Jogador {user} vencedor!')
            mostra_dic(dicio)
            return 'fecha'

    if (dicio['top-l'] and dicio['mid-m'] and dicio['low-r'] != ' ') and (dicio['top-l'] == dicio['mid-m'] == dicio['low-r']):
            print('-'*3)
            print(f'Jogador {user} vencedor!')
            mostra_dic(dicio)
            return 'fecha'
    
    if (dicio['top-r'] and dicio['mid-m'] and dicio['low-l'] != ' ') and (dicio['top-r'] == dicio['mid-m'] == dicio['low-l']):
        print('-'*3)
        print(f'Jogador {user} vencedor!')
        mostra_dic(dicio)
        return 'fecha'


dicio = {'top-l': ' ', 'mid-l': ' ', 'low-l': ' ', 
        'top-m': ' ', 'mid-m': ' ', 'low-m': ' ', 
        'top-r': ' ', 'mid-r': ' ', 'low-r': ' '
        }

user = 'O'
a = ''
while True:
    
    mostra_dic(dicio)

    x = input(f'Vez de {user}: ')
    dicio[x] = user #atribuo o valor 'user' para o campo input dado
    
    #função retorna valor que indica
    #se o laço deve ser parado ou não
    a = confere_vencedor(dicio, user)

    #confere se há comando para pausa do laço
    if a == 'fecha': 
        break

    #troca user
    if user == 'O': 
        user = 'X'
    else:
        user = "O"


'''
   
'''