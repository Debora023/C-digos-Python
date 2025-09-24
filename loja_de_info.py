#requisitos:
#1-cadastro cliente. 
#2-cadastro de tipo de serviço
#3-cadastro de ordem de serviço, com o problema.
#4-controle de produtos no estoque (colocar e retirar do estoque)
#5- " fale conosco: " para tirar duvida referente ao serviço
#6-relatorios do tipo de serviço (puxar lista)
#7-enviar notificação pós exceder o prazo    
 
from dataclasses import dataclass
from datetime import datetime
 
@dataclass

class Cadastro_cliente:
     nome:str
     numero: str
     
lista_Cadastro = []
lista_de_Servico = []
lista_de_Os = []
class Cadastro_de_Servico:
     formatacao:str
     limpeza_geral:str
     trocas_de_pecas:str 
     remocao_de_virus:str
     instalacao_de_programas:str

 def Cadastro_de_Os():
    nome_cliente = input("Qual o nome do cliente")
    problema = input("Qual o problema dele")
    cadastro_de_Servico  = Cadastro_de_Servico (formatacao,limpeza_geral,troca_de_pecas,remocao_de_virus,instalacao_de_programas)
    print("Qual o problema da sua máquina?")
    
def menu():
    print("\n--- COMPUTARIA supports.INFO ---")
    print("1 - Cadastro Cliente")
    print("2 - Cadastro de serviço")
    print("3 - Ordem de serviço")
    print("4 - Controle de estoque")
    print("5 - Fale conosco")
    print("6 - Relatório")
    print("0 - Sair")
    return input("Escolha uma opção: ")
    
while True:
    
     opcao = menu()

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        numero = input("Digite o número do cliente: "))
        print(f" Cliente cadastrado com sucesso!")

    elif opcao == "2":
        if nome is None:
            print("Nenhum cadastro de serviço feito!")
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
    
    
    
    
    
    
    
    
    
