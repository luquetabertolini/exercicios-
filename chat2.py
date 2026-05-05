maior = 0
menor = 0
primeiro = True

while True:
    n = int(input(f' Digite um número: '))
    if n == 0:
        print('Encerrando o programa...')
        break

    if primeiro:
        maior = n
        menor = n
        primeiro = False
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f' Maior = {maior}')
print(f' Menor = {menor}')
