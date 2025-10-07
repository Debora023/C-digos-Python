from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cadastro:
    usuario: str
    email: str
    numero: int

lista_cadastro = []

class agendamento:
    nome: str
    corte: str
    horario: str
    email: str
    barbeiro: str

lista_cortes = []

def criar_usuario():
    nome = input("Qual o seu nome: ")
    email = input("Qual o seu email: ")
    numero = input("Qual é seu número: ")
    cadastro_digitado = Cadastro(nome,email,numero)
    lista_cadastro.append(cadastro_digitado)
    print("Cadastro efetuado com sucesso")

def fazer_login():
    login_email = input("Qual o seu email: ")
    login_numero = input("Qual é seu número: ")
    
    for usuario in lista_cadastro:
        if usuario.email == login_email:
            if usuario.numero == login_numero:
                print("Acesso autorizado")
            else:
                print("Email ou número incorreto")
        
def agendamento():
    corte = input("Qual corte vc vai querer: ")
    barbeiro = input("Qual barbeiro vc quer: ")
    horario = input("Digite o horário do corte: ")

def cadastro_servico():
    nome_do_corte = input("Coloque o corte que você quer adicionar: ")
    descricao = input("Descreva o corte: ")
    valor = input("Digite o valor do corte: ")
    print(f"O corte {nome_do_corte} foi cadastrado com sucesso!")

def faleconosco():
    ajuda = input("Digite sua dúvida: ")
    print("Enviamos um email para você")
    

def menu():
    print("\n--- ✂ Barbearia Déyan ✂ ---")
    print("1 - Cadastro ")
    print("2 - Login ")
    print("3 - Agendamento ")
    print("4 - Cadastro de serviço ")
    print("5 - Fale conosco ")
    print("6 - Sair")
    return input("Escolha uma opção: ")
    
while True:
    opcao = menu()
    if opcao == "1":
        criar_usuario()
    
    elif opcao == "2":
        fazer_login()
    
    elif opcao == "3":
        agendamento()
        
    elif opcao == "4":
        cadastro_servico()
    
    elif opcao == "5":
        faleconosco()
        
    elif opcao == "6":
        print("Saindo... Até mais tarde")
        break
    else:
        print("Tente mais tarde")
