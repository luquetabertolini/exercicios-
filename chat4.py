quantidade_par = 0

while True:
    n = int(input(f' Digite o número desejado: '))
    if n == 0:
        print(f' Encerrando programa...')
        break

    if n % 2 == 0:
        quantidade_par += 1

print(f' Quantidade de pares digitados (sem contar o 0): {quantidade_par}')