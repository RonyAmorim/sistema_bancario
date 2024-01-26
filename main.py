# This is a sample Python script.
import os

def realizar_saque(saldo, limite, numero_saques, LIMITE_SAQUES,extrato):
    valor = float(input('\nDigite o valor a ser sacado: '))

    if valor > saldo:
        print(f'Você não possui R${valor:.2f} disponível. Seu saldo é de R${saldo:.2f}')
    elif valor > limite:
        print(f'O valor máximo permitido para saque é de R$ {limite:.2f}')
    elif numero_saques < LIMITE_SAQUES:
        numero_saques += 1
        saldo -= valor
        extrato += f"Saque - R${valor:.2f}\n"
        print(f"Saque no valor de R${valor:.2f} realizado!")

    return saldo, numero_saques, extrato

def realizar_deposito (saldo, extrato):
    valor = float(input("\nDigite o valor a ser depositado: "))

    while valor <= 0:
        print('Não é possível realizar depósitos menores de R$ 1,00')
        valor = float(input('\nDigite o valor desejado: '))

    saldo += valor
    extrato += f"Depósito - R${valor:.2f}\n"
    print('\nDepósito realizado!')

    return saldo, extrato

def exibir_extrato(extrato):
    if not extrato:
        print('\nNão foram realizadas movimentações')
    else:
        print(f'\n{extrato}')


saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    os.system('cls')
    opcao = int(input('\n      Menu\n\n'
                      f'Saldo: R${saldo:.2f}\n\n'
                      '1 - Saque\n'
                      '2 - Deposito\n'
                      '3 - Extrato\n'
                      '4 - Sair\n\n'
                      'Digite uma opção: '))

    if opcao == 1:
        saldo, numero_saques, extrato = realizar_saque(saldo, limite, numero_saques, LIMITE_SAQUES, extrato)
    elif opcao == 2:
        saldo, extrato = realizar_deposito(saldo,extrato)
    elif opcao == 3:
        exibir_extrato(extrato)
    elif opcao == 4:
        print("\nEncerrando o programa!")
        break
    else:
        print("\nOpção inválida. Tente Novamente.")
