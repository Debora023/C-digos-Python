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
        cadastro_cliente()
        
    opcao = menu()
    if opcao == "1":
        ()
