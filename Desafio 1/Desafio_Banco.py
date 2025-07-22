menu = """
+==============================+
|""" + "MENU".center(30) + """|
+==============================+
| [d] Depositar                |
| [s] Sacar                    |
| [e] Extrato                  |
| [q] Sair                     |
+==============================+

Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("Bem-vindo ao Banco do Jefe!")
print("Sistema bancário personalizado iniciado...\n")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")

        else:
            print("Eita! Valor inválido, tenta de novo aí!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Relaxa aí! Você não tem essa grana toda não...")

        elif excedeu_limite:
            print("Opa! Limite de R$ 500 por saque, respeita!")

        elif excedeu_saques:
            print("Calma lá! Só 3 saques por dia, já deu por hoje!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque liberado! Sobrou: R$ {saldo:.2f}")

        else:
            print("Eita! Valor inválido, tenta de novo aí!")

    elif opcao == "e":
        print("\n" + "="*40)
        print("EXTRATO".center(40))
        print("="*40)
        print("Nenhuma movimentação ainda..." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        saques_restantes = LIMITE_SAQUES - numero_saques
        print(f"Saques restantes hoje: {saques_restantes}")
        print("="*40 + "\n")

    elif opcao == "q":
        print("\nValeu! Volte sempre ao Banco do Jefe!")
        break

    else:
        print("Opção inválida! Escolhe direito aí, parceiro!")
