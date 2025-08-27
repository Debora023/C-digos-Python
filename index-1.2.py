def menu():
    print("\n--- Sistema de Estoque ---")
    print("1 - Cadastrar evento")
    print("2 - Retirar ingressos")
    print("3 - Adicionar ingressos")
    print("4 - Ver quantidade de ingressos em estoque")
    print("0 - Sair")
    return input("Escolha uma opção: ")


nome = None
horario = None
quantidade = 0

while True:
    opcao = menu()

    if opcao == "1":
        nome = input("Digite o nome do evento: ")
        horario = input("Digite o horário do evento: ")
        quantidade = int(input("Digite a quantidade de ingressos: "))
        print(f"Evento {nome}, às {horario} com {quantidade} ingressos cadastrado com sucesso!")

    elif opcao == "2":
        if nome is None:
            print("Nenhum evento cadastrados ainda!")
        else:
            retirar = int(input("Digite a quantidade de ingressos a retirar: "))
            if retirar <= 0:
                print("A quantidade deve ser maior que zero!")
            elif retirar > quantidade:
                print("Quantidade insuficiente no estoque!")
            else:
                quantidade -= retirar
                print(f"Retirado {retirar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "3":
        if nome is None:
            print("Nenhum evento cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} ingresso(s). Estoque atual: {quantidade}")

    elif opcao == "4":
        if nome is None:
            print("Nenhum evento cadastrado ainda!")
        else:
            print(f"Evento {nome} | Quantidade em estoque: {quantidade}")

    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")