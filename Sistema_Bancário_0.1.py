menu = """"
    Menu Principal

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
"""
saldo = 0.0
limite = 1000
extrato = ""
LIMITE_SAQUES = 5

while True:
    opção = input(menu)

    if opção == "1":
        print("Depositar")
        valor = float(input("Insira o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! o valor informado é inválido.")

    elif opção == "2":
            print("Sacar")
            valor = float(input("Insira o valor de saque: "))
            if LIMITE_SAQUES > 0 and valor < 500 and valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                LIMITE_SAQUES -= 1
            elif valor > 500:
                print(f"Valor máximo disponivel para saque: {limite}")
            elif LIMITE_SAQUES == 0:
                print("Valor de saques diários excedido") 
            else:
                print("Operação falhou! o valor informado é inválido.")

    elif opção == "3":
        print("Extrato")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"Saldo total de: {saldo}")
        
    elif opção == "4":
        print("Sair")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")