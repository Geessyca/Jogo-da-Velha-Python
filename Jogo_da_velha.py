#!/usr/bin/env python
# coding: utf-8

# In[1]:


tab = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
valido = True
jogo_continua = True
Velha = ('velha')

 
def tabuleiro():
      print("\n",'0 | 1 | 2 ',"   |     ", tab[0], '|', tab[1], '|', tab[2])
      print('-' * 11, "   |    ",'-' * 11)
      print(' 3 | 4 | 5 ',"   |     ",tab[3], '|', tab[4], '|', tab[5])
      print('-' * 11, "   |    ",'-' * 11)
      print(' 6 | 7 | 8 ',"   |     ",tab[6], '|', tab[7], '|', tab[8],"\n")

def jogador_x () :
    global valido
    print ('Vez de X')
    posicao = input('Escolha uma posicao: ')
    while posicao not in ['0','1', '2', '3', '4', '5', '6', '7', '8']:
        print ('Entrada não válida')
        posicao = input('Escolha uma posicao:')
    posicao.isnumeric()
    while posicao.isnumeric() == False:
        posicao = input('Escolha uma posicao:')
    posicao = int(posicao)
    tab[posicao].isupper
    while tab[posicao].isupper() == True:
        print ('Posição não válida')
        posicao = input('Escolha uma posição')
        posicao = int(posicao)
    tab[posicao] = 'X'
    tabuleiro ()
    check_vencedor ()
    if jogo_continua == False:
        menu()
    if jogo_continua == True:
            jogador_o ()

def jogador_o () :
    global valido
    print ('Vez de O')
    posicao = input('Escolha uma posicao: ')
    while posicao not in ['0','1', '2', '3', '4', '5', '6', '7', '8']:
        posicao = input('Escolha uma posicao:')
    while posicao.isnumeric() == False:
        posicao = input('Escolha uma posicao:')
    posicao = int(posicao)
    tab[posicao].isupper
    if tab[posicao].isupper() == True:
        print ('Posição nao válida')
        posicao = input('Escolha uma posição')
        posicao = int(posicao)
    tab[posicao] = 'O'
    tabuleiro ()
    check_vencedor ()
    if jogo_continua == False:
        menu()
    if jogo_continua == True:
        jogador_x ()
        

def check_vencedor () :
    vencedor_linha = linha()
    vencedor_vertical = vertical ()
    vencedor_diagonais = diagonais ()
    velha = deu_velha ()
    if vencedor_linha:
        print ('O vencedor é: {}'.format(vencedor_linha))
    elif vencedor_vertical:
        print ('O vencedor é: {}'.format (vencedor_vertical))
    elif vencedor_diagonais:
        print ('O vencedor é: {}'.format (vencedor_diagonais))
    elif velha:
        print ('O jogo deu velha')

def linha () :
    global jogo_continua
    linha_1 = tab[0] == tab[1] == tab[2] != '-'
    linha_2 = tab[3] == tab[4] == tab[5] != '-'
    linha_3 = tab[6] == tab[7] == tab[8] != '-'
    if linha_1 or linha_2 or linha_3: 
        jogo_continua = False
    if linha_1:
        return tab[0] 
    elif linha_2:
        return tab[3] 
    elif linha_3:
        return tab[6] 
    else:
        return None

def vertical () :
    global jogo_continua
    vertical_1 = tab[0] == tab[3] == tab[6] != '-'
    vertical_2 = tab[1] == tab[4] == tab[7] != '-'
    vertical_3 = tab[2] == tab[5] == tab[8] != '-'
    if vertical_1 or vertical_2 or vertical_3:
        jogo_continua = False
    if vertical_1:
        return tab[0]
    elif vertical_2:
        return tab[1]
    elif vertical_3:
        return tab[2]
    else:
        return None

def diagonais () :
    global jogo_continua
    diagonal_1 = tab[0] == tab[4] == tab[8] != '-'
    diagonal_2 = tab[2] == tab[4] == tab[6] != '-'
    if diagonal_1 or diagonal_2:
        jogo_continua = False
    if diagonal_1:
        return tab[0]
    elif diagonal_2:
        return tab[2]
    else:
        return None

def deu_velha () :
    global jogo_continua
    if '-' not in tab:
        jogo_continua = False
        return Velha
    else:
        return None
def menu():
    dnv = str(input('Deseja jogar novamente? [S] [N]'))
    if dnv == 's' or dnv == 'S' or dnv == 'n' or dnv == 'N':
        dnv = str(dnv)
    else:
        print ('Entrada não válida')
        dnv = str(input('Deseja jogar novamente? [S] [N]'))
    while dnv not in['s','S','n','N']:
        print ('Entrada não válida')
        dnv = str(input('Deseja jogar novamente? [S] [N]'))
    if dnv=='s' or dnv=='S' :
        tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        jogo_continua = True
        boasvindas()
    if dnv=='n' or dnv=='N':
        quit()

def jogar1 () :
    tabuleiro()
    jogador_x ()

def boasvindas():
    print("\n°°°°°°°°°°°°  BEM VINDO AO NOSSO JOGO DA VELHA  °°°°°°°°°°°°\n")
    jogar1()

boasvindas()


# In[ ]:




