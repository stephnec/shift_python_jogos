# -*- enconding: utf-8 -*-
import random

def jogar():
    # Exibindo o cabeçalho do jogo
    print('***********************************')
    print('* Bem vindo ao Jogo da Advinhação *')
    print('***********************************')


    numero_secreto = random.randint(1,100)
    pontos = 1000

    while True:
        print('Qual nível você deseja participar?')
        print('Digite: 1 - Fácil | 2 -  Intermediário | 3 - Dificil')
        nivel = int(input('Escolha seu nível: '))

        if nivel == 1 or nivel == 2 or nivel == 3:
            break

        print('O nível deve ser escolhido de acordo com as opções oferecidas.')

    tentativa = 1
    max_tentativas = 3


    if nivel == 1:
        max_tentativas = 10
    elif nivel == 2:
        max_tentativas = 5
    elif nivel == 3:
        max_tentativas = 3

    print(numero_secreto)
    
    while tentativa <= max_tentativas:
        print(f'Tentativa {tentativa} de {max_tentativas}') # f-string
        numero_escolhido = input('Escolha o número secreto: ')
        numero_escolhido = int(numero_escolhido)


        if numero_escolhido < 1 or numero_escolhido > 100:
            print('Só aceito números entre 1 e 100.')
            continue

        acertou = numero_escolhido == numero_secreto

        maior = numero_escolhido < numero_secreto
        menor = numero_escolhido > numero_secreto
        

        if acertou:
            print('Parabéns! Você acertou o número.')
            print(f'Sua pontuação foi de {pontos} pontos.')
            break
        else:
            print('Errou!')
            if maior:
                print('O número secreto é maior que o escolhido')
            elif menor:
                print('O número secreto é menor que o escolhido ')
            pontos_perdidos = abs(numero_escolhido - numero_secreto)
            pontos -= pontos_perdidos

        tentativa += 1


    if not acertou:
        print(f'O número secreto era {numero_secreto}.')

    print('Fim de Jogo')


if __name__ == '__main__':
    jogar()