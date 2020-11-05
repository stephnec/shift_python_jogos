# -*- enconding: utf-8 -*-
import random


def jogar():
    # Exibindo o cabeçalho do jogo
    print('***********************************')
    print('*   Bem vindo ao Jogo da Forca    *')
    print('***********************************')

    palavras = []
    with open('.\\palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randint(0, len(palavras) - 1)].upper()
    print(palavra_secreta)
    # List Comprehensions
    letras_corretas = ['_' for letra in palavra_secreta]
    letras_escolhidas = []

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        print(letras_corretas)
        letra = input('Informe uma letra: ')
        letra = letra.strip().upper()

        if letra in letras_escolhidas:
            print('Você já falou essa letra.')
            continue
        else:
            letras_escolhidas.append(letra)

        if letra in palavra_secreta:
            indice = 0
            for l in palavra_secreta:
                if l == letra:
                    letras_corretas[indice] = letra
                indice += 1
        else:
            print('Essa letra não existe na palavra')
            erros += 1

        acertou = '_' not in letras_corretas
        enforcou = erros == len(palavra_secreta)

    print(f'A palavra era {palavra_secreta}.')
    if acertou:
        print('Parabéns! Você acertou a palavra secreta')
    else:
        print('Ops... Tente novamente')
    

if __name__ == '__main__':
    jogar()