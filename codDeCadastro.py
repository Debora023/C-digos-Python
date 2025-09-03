from dataclasses import dataclass

@dataclass
class Cadastro:
    usuario: str
    email: str
    senha: int
    data_de_nasc: str
    ativo: bool
    
lista = []

def criar_usuario():
    nome = input("Qual o seu nome: ")
    email = input("Qual o seu email: ")
    senha = input("Qual a sua senha: ")
    usuario_digitado = Usuario(nome,email,senha)
    lista.append(usuario_digitado)
    print("Cadastro efetuado com sucesso")

def pesquisar_email():
    nome_digitado = input("Qual o seu nome: ")
    for usuario in lista:
        if usuario.nome == nome_digitado:
            print(f"email desse usuario -> {usuario.email}")
            
def fazer_login():
    login_email = input("Qual o seu email: ")
    login_senha = input("Qual a sua senha: ")
    
    for usuario in lista:
        if usuario.email == login_email:
            if usuario.senha == login_senha:
                print("Acesso autorizado")
            else:
                print("Email ou senha incorreto")
        else:
            print("Email ou senha incorreto")
def menu():
    print("\n--- Cadrastro ---")
    print("1 - Login ")
    print("2 - Buscar email")
    print("3 - Sair")
    return input("Escolha uma opção: ")
    
while True:
    opcao = menu()
    if opcao == "1":
        criar_usuario()
    
    elif opcao == "2":
        fazer_login()
        
    elif opcao == "3":
        pesquisar_email()
        
    elif opcao == "4":
        break

    
usuario1 = Cadastro("Homem aranha", "Peterzinreidelas@hotemail.com",1166, "15/08/1990", True)
usuario2 = Cadastro("Cavaleiro da lua", "Pequenoprinceso@gmail.com", 4040, "00/00/0000", True)
usuario3 = Cadastro("Batman", "Batmóvel@gmail.com", 5893, "19/02/1985", True)

lista_de_cadastro = []
lista_de_cadastro.append(usuario1)
lista_de_cadastro.append(usuario2)
lista_de_cadastro.append(usuario3)
 
print(lista_de_cadastro)

digite = int(input("\nQual login você gostaria de entrar? \n1 - usuario1 \n2 - usuario2 \n3 - usuario3 \n"))
print(lista_de_cadastro[digite-1])
