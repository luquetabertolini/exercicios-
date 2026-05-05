quantidade_numero = 0
quantidade_par = 0
quantidade_impar = 0
soma = 0

while True:
    n = int(input(f' Digite um número: '))
    if n == 0:
        print(f' Programa encerrando...')
        break


    if n % 2 == 0:
        quantidade_par += 1
    else:
        quantidade_impar += 1

    soma += n
    quantidade_numero += 1

if quantidade_numero > 0:
    media = soma / quantidade_numero
else:
    media = 0

print(f' Números digitados: {quantidade_numero}')
print()
print(f' Números pares digitados: {quantidade_par}')
print()
print(f' Números ímpares digitados: {quantidade_impar}')
print()
print(f' Soma dos números digitados: {soma}')
print()
print(f' Média dos números digitados: {media}')


