tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = int(input('Digite a senha: '))
    tentativas += 1
    tentativas_restantes = max_tentativas - tentativas

    if senha == 1234:
        print('Acesso liberado.')
        break
    else:
        print('Acesso negado.')
        print()
        print(f'Tentativas restantes: {tentativas_restantes}')

if senha != 1234:
    print('Tente novamente mais tarde...')