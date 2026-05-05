def somar_numeros():
    print(' Iniciando programa de soma...\n')
    soma = 0

    while True:
        n = int(input(' Digite o número desejado: '))
        if n <= 0:
            print(' Programa encerrando...')
            break
        soma += n

    print(f' A soma é de {soma}\n')


def contar_pares():
    print(' Iniciando programa de contar pares...\n')
    print(' Digite números positivos (0 encerra)')
    quantidade_par = 0

    while True:
        n = int(input(' Digite o número desejado: '))
        if n == 0:
            print(' Programa encerrando...')
            break
        elif n % 2 == 0:
            quantidade_par += 1

    print(f' A quantidade de pares é de: {quantidade_par}\n')


def menu():
    while True:
        print(' Escolha uma das opções abaixo:\n')
        print(' 1 - Somar números')
        print(' 2 - Contar pares')
        print(' 3 - Sair')

        escolha = int(input(' O que deseja? '))

        if escolha == 1:
            somar_numeros()
        elif escolha == 2:
            contar_pares()
        elif escolha == 3:
            print(' Saindo...')
            break
        else:
            print(' Escolha inválida, tente novamente.\n')


# iniciar sistema
menu()