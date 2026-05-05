# Menu
while True:
    print(' Escolha uma das opções abaixo:\n')
    print(' 1 - Somar números')
    print(' 2 - Contar pares')
    print(' 3 - Sair')

    escolha = int(input(' O que deseja? '))

# Validar Escolha
    if escolha < 1 or escolha > 3:
        print(' Escolha inválida, tente novamente.\n')

# Programa de soma
    elif escolha == 1:
        print(' Iniciando programa de soma...\n')
        soma = 0

        while True:
            n = int(input(f' Digite o número desejado: '))
            if n <= 0:
                print(f' Programa encerrando...')
                break
            soma += n
        print(f' A soma é de {soma}\n')

# Programa de pares
    elif escolha == 2:
        print(f' Iniciando programa de contar pares...\n')
        print(f' Digite números positivos (0 ou negativo encerra)')
        quantidade_par = 0

        while True:
            n = int(input(f' Digite o número desejado: '))
            if n == 0:
                print(f' Programa encerrando...')
                break
            elif n % 2 == 0:
                quantidade_par += 1
        print(f' A quantidade de pares é de: {quantidade_par}')
    else:
        print(' Saindo...')
        break
