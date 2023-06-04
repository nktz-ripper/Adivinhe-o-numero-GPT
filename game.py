# Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 10, e 
# o usuário tem 5 tentativas para adivinhar o número

import random

def game():
    tentativas = 5
    generated_number = random.choice(range(11))
    
    # This is the cheat code
    # print(generated_number)

    while (tentativas != 0) == True:
        try:
            print(f'\nO gênio GPT pensou em um número de 0 a 10. Você precisa adivinhar qual é.\nVocê tem {tentativas} tentativas restantes.\n')
            resposta = int(input('Sua resposta: '))
            if int(resposta) == int(generated_number):
                print(f'---- Não acredito! Você ganhou! Você ainda tinha {tentativas} tentativas restantes!')
                tentativas = 0
            elif int(resposta) > 10:
                print(f'---- Número fora do intervalo de 0 a 10.')
            elif int(resposta) < 0:
                print(f'---- Número fora do intervalo de 0 a 10.')
            else:
                print('---- NEGATIVO, tente novamente.')
                tentativas = tentativas - 1
        except ValueError:
            print(f'---- Input inválido. Tente novamente.') 
    else:
        print(f'Fim de jogo.\nA resposta correta era {generated_number}.')
        if input("Deseja jogar novamente? (y/n) ") != "n":
            game()
        else:
            print('Obrigado.')
            
game()