def ver_saldo(saldo):
    print(f' Seu saldo atual é {saldo:.2f}\n')

def depositar(saldo):
    valor = float(input(f' Digite o valor para depósito em R$: \n'))

    if valor <= 0:
        print(f' Valor inválido!\n')
    else:
        saldo += valor
        print(f' Seu depósito foi um sucesso! Saldo atual: R${saldo}\n')

    return saldo

def sacar(saldo):
    valor = float(input(f' Digite o valor para saque em R$: \n'))

    if valor <= 0:
        print(f' Valor inválido!\n')
    elif valor > saldo:
        print(f' Saldo insuficiente!\n')
    else:
        saldo -= valor
        print(f' Saque realizado! Novo saldo: R${saldo}\n')

    return saldo

def menu():
    saldo = 0

    while True:
        print(f'==== BANCO ====\n')
        print(f' 1 - Ver saldo')
        print(f' 2 - Depositar')
        print(f' 3 - Sacar')
        print(f' 4 - Sair')

        escolha = (input(f' Digita a opção desejada: '))

        if escolha == '1':
            ver_saldo(saldo)
        elif escolha == '2':
            saldo = depositar(saldo)
        elif escolha == '3':
            saldo = sacar(saldo)
        elif escolha == '4':
            print(f' Saindo...')
            break

        else:
            print(f' Opção inválida\n')

menu()