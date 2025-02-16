def exibir_menu():
    print("\n***** Bem-vindo ao Banco do Programador! *****")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    return input("Escolha uma opção: ")

def consultar_saldo(saldo):
    print(f"\nSeu saldo é R$ {saldo:.2f}")

def depositar(saldo):
    try:
        valor = float(input("\nDigite o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            print(f"Depósito realizado com sucesso! Seu saldo é R$ {saldo:.2f}")
        else:
            print("Valor inválido! O depósito deve ser maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
    return saldo

def sacar(saldo):
    try:
        valor = float(input("\nDigite o valor a ser sacado: R$ "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            print(f"Saque realizado com sucesso! Seu saldo é R$ {saldo:.2f}")
        elif valor > saldo:
            print("Saldo insuficiente! Tente novamente.")
        else:
            print("Valor inválido! O saque deve ser maior que zero.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
    return saldo

def main():
    saldo = 5000.00  # Saldo inicial
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            consultar_saldo(saldo)
        elif opcao == "2":
            saldo = depositar(saldo)
        elif opcao == "3":
            saldo = sacar(saldo)
        elif opcao == "4":
            print("Obrigado por utilizar o Banco do Programador!")
            break
        else:
            print("Opção inválida! Tente novamente.")

        retorno = input("\nDeseja voltar ao menu principal? (s/n): ").strip().lower()
        if retorno != 's':
            print("Obrigado por utilizar o Banco do Programador!")
            break

if __name__ == "__main__":
    main()
