import random
numero = random.randint(1, 10)

tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    adv = int(input(' Adivinhe o número de 1 a 10: '))
    tentativas += 1

    if adv < numero:
        print(' Maior.')
        print()
    elif adv > numero:
        print(' Menor.')
        print()
    else:
        print(' ACERTOU!')
        break

if adv == numero:
    print(f' Tentativas: {tentativas}') 
else:
    print(' Você perdeu!')
    print(f' O número era: {numero}')