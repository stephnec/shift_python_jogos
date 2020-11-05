# -*- enconding: utf-8 -*-

from jogos import advinhacao, forca

print('***********************************')
print('*   Bem vindo! Escolha um jogo    *')
print('***********************************')

while True:
    print('Qual jogo você quer jogar?')
    print('Digite: 1 - Jogo da Advinhação | 2 -  Jogo da Forca')
    jogo =  int(input('Escolha o Jogo: '))


    if jogo == 1:
        advinhacao.jogar()
        break
    elif jogo == 2:
        forca.jogar()
        break
    else:
        print('Jogo fora de catálogo...')


