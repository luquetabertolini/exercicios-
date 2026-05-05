soma = 0
quantidade = 0

while True:
    n = int(input('Digite um número: '))
    print()

    if n <= 0:
        print('Programa encerrando...')
        break

    soma += n
    quantidade += 1

print()

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print(f'Soma = {soma}')
print()
print(f'Quantidade = {quantidade}')
print()
print(f'Média = {media}')