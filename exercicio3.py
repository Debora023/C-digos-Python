from dataclasses import dataclass
from datetime import datetime

@dataclass
class Publicacao:
    conteudo: str
    descricao: str
    autor: str
    data_hora: datetime
    curtidas: int = 0
    republicar: int = 0

lista_publicacoes = []

def criar_publicacao():
    print("\n--- CRIAR PUBLICAÇÃO ---")
    conteudo = input("Digite o conteúdo da publicação: ")
    descricao = input("Dê uma descrição ao post: ")
    autor = input("Digite o nome do criador: ")
    data_hora = datetime.now()

    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)
    print("Publicação criada com sucesso!")

def curtir_publicacao():
    print("\n--- CURTIR PUBLICAÇÃO ---")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return

    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para curtir: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].curtidas += 1
            print("Você curtiu a publicação!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

def republicar_publicacao():
    print("\n--- REPUBLICAR PUBLICAÇÃO ---")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return

    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para republicar: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].republicar += 1
            print("Publicação republicada!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

def visualizar_feed():
    print("\n=== FEED ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return

    for i, pub in enumerate(lista_publicacoes, 1):
        print(f"{i}. {pub.autor} - {pub.curtidas} curtidas - {pub.republicar} republicações")
        print(f"  {pub.conteudo[:50]}...")
        print(f"  {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 40)

def visualizar_publicacao_individual():
    print("\n=== VISUALIZAR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação.")
        return

    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            print(f"\nAutor: {pub.autor}")
            print(f"Data: {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print(f"Conteúdo: {pub.conteudo}")
            print(f"Descrição: {pub.descricao}")
            print(f"Curtidas: {pub.curtidas}")
            print(f"Republicações: {pub.republicar}")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

def visualizar_publicacoes_por_autor():
    print("\n=== PUBLICAÇÕES POR AUTOR ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return

    autor = input("Digite o nome do autor: ")
    publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()]

    if not publicacoes_autor:
        print(f"Nenhuma publicação encontrada para {autor}.")
        return

    print(f"\nPublicações de {autor}:")
    for pub in publicacoes_autor:
        print(f"- {pub.conteudo[:50]}... ({pub.curtidas} curtidas)")
        print(f"  {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 30)

def menu():
    while True:
        print("\n=== REDE SOCIAL ===")
        print("1. Criar Publicação")
        print("2. Curtir Publicação")
        print("3. Republicar Publicação")
        print("4. Visualizar Feed")
        print("5. Visualizar Publicação Individual")
        print("6. Visualizar Publicações por Autor")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_publicacao()
        elif opcao == "2":
            curtir_publicacao()
        elif opcao == "3":
            republicar_publicacao()
        elif opcao == "4":
            visualizar_feed()
        elif opcao == "5":
            visualizar_publicacao_individual()
        elif opcao == "6":
            visualizar_publicacoes_por_autor()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

