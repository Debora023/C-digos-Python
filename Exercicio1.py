#Exercicio 1
#Sistema de estoque com apenas 1 produto
#1. Opção de cadastro do nome do produto.
#2. Opção de retirar produto do estoque (precisa ver se tem o produto)
#3. Opção de adicionar produto no estoque (precisa adicionar um numero maior que 0)
#4. Opção de ver a quantidade no estoque


def menu():
    print("\n--- Sistema de Estoque---")
    print("1 - Cadastrar Produto")
    print("2 - Retirar do Estoque")
    print("3 - Adicionar ao Estoque")
    print("4 - Ver quantidade em estoque")
    print("0 - Sair")
    return input("Escolha uma opção: ")

produto = None
quantidade = 0

while True:
    opcao = menu()

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = 0
        print(f"Produto '{produto}' cadastrado com sucesso!")

    elif opcao == "2":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            retirar = int(input("Digite a quantidade a retirar: "))
            if retirar <= 0:
                print("A quantidade deve ser maior que zero!")
            elif retirar > quantidade:
                print("Quantidade insuficiente no estoque!")
            else:
                quantidade -= retirar
                print(f"Retirado {retirar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "3":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "4":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            print(f"Produto: {produto} | Quantidade em estoque: {quantidade}")

    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
