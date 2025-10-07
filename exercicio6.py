from dataclasses import dataclass, field
from datetime import datetime, timedelta

@dataclass
class Servico:
    nome: str
    preco: float
    cobranca_peca: bool = False

@dataclass
class ItemEstoque:
    nome: str
    quantidade: int
    preco_custo: float

@dataclass
class Tecnico:
    nome: str
    especialidade: str
    produtividade: int = 0

@dataclass
class OrdemServico:
    cliente: str
    equipamento: str
    problema: str
    servicos_solicitados: list[str] = field(default_factory=list)
    tecnico_responsavel: str = ""
    status: str = "Em análise"
    data_entrada: datetime = field(default_factory=datetime.now)
    data_conclusao: datetime = None
    valor_total: float = 0.0
    itens_utilizados: list[str] = field(default_factory=list)

servicos_disponiveis = [
    Servico("Formatação", 80.0),
    Servico("Limpeza Geral", 50.0),
    Servico("Troca de Peças", 0.0, True),
    Servico("Remoção de Vírus", 60.0),
    Servico("Instalação de Programas", 40.0),
]

estoque = [
    ItemEstoque("Memória RAM", 10, 80.0),
    ItemEstoque("SSD", 5, 120.0),
    ItemEstoque("Fonte", 8, 95.0),
]

lista_tecnicos = [
    Tecnico("Eu", "Hardware/Software"),
    Tecnico("Marido", "Hardware/Software"),
    Tecnico("João", "Hardware"),
    Tecnico("Maria", "Software"),
]

ordens_de_servico = []
taxa_avaliacao = 30.0
taxa_armazenamento_diaria = 10.0

def criar_ordem_servico():
    print("\n--- Criação de Ordem de Serviço ---")
    cliente = input("Nome do cliente: ")
    equipamento = input("Tipo de equipamento: ")
    problema = input("Descrição do problema: ")

    nova_os = OrdemServico(cliente, equipamento, problema)
    ordens_de_servico.append(nova_os)
    print("✅ Ordem de serviço criada com sucesso. Status: Em análise.")

def criar_orcamento(os_selecionada: OrdemServico):
    print("\n--- Criando Orçamento ---")
    servicos_selecionados = []
    valor_servicos = 0.0

    print("Serviços disponíveis:")
    for i, servico in enumerate(servicos_disponiveis, 1):
        print(f"{i} - {servico.nome} (R${servico.preco:.2f})")

    while True:
        escolha = input("Escolha o serviço (ou 's' para sair): ")
        if escolha.lower() == 's':
            break
        try:
            servico_escolhido = servicos_disponiveis[int(escolha) - 1]
            servicos_selecionados.append(servico_escolhido)
            print(f"✅ '{servico_escolhido.nome}' adicionado.")
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")

    for servico in servicos_selecionados:
        if servico.cobranca_peca:
            print("\n--- Troca de Peças ---")
            print("Peças em estoque:")
            for i, item in enumerate(estoque, 1):
                print(f"{i} - {item.nome} | Quantidade: {item.quantidade} | Preço de Custo: R${item.preco_custo:.2f}")
            
            try:
                peca_escolhida = int(input("Escolha a peça a ser trocada: ")) - 1
                item_estoque = estoque[peca_escolhida]
                if item_estoque.quantidade > 0:
                    preco_peca_final = item_estoque.preco_custo * 1.3
                    valor_servicos += preco_peca_final
                    os_selecionada.itens_utilizados.append(item_estoque.nome)
                    item_estoque.quantidade -= 1
                    print(f"Peça '{item_estoque.nome}' adicionada ao orçamento (R${preco_peca_final:.2f}).")
                else:
                    print(f"Peça '{item_estoque.nome}' está fora de estoque.")
            except (ValueError, IndexError):
                print("Opção de peça inválida.")
        else:
            valor_servicos += servico.preco
    
    os_selecionada.valor_total = valor_servicos
    os_selecionada.servicos_solicitados = [s.nome for s in servicos_selecionados]
    print(f"\n✅ Orçamento final: R${os_selecionada.valor_total:.2f}")

    aprovar = input("O cliente aprovou o orçamento? (s/n): ").lower()
    if aprovar == 's':
        os_selecionada.status = "Aprovado"
        print("Status atualizado para 'Aprovado'.")
    else:
        print(f"Serviço não aprovado. Cobrar taxa de avaliação: R${taxa_avaliacao:.2f}")
        os_selecionada.valor_total = taxa_avaliacao
        os_selecionada.status = "Não Aprovado"

def gerenciar_os():
    print("\n--- Gerenciar Ordem de Serviço ---")
    if not ordens_de_servico:
        print("Não há ordens de serviço ativas.")
        return

    print("Ordens de Serviço ativas:")
    for i, os in enumerate(ordens_de_servico, 1):
        print(f"{i} - Cliente: {os.cliente} | Equipamento: {os.equipamento} | Status: {os.status}")

    try:
        escolha = int(input("Escolha a ordem de serviço para gerenciar: ")) - 1
        os_selecionada = ordens_de_servico[escolha]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    print(f"\nDetalhes da OS de {os_selecionada.cliente}:")
    print(f"Status Atual: {os_selecionada.status}")

    if os_selecionada.status == "Em análise":
        criar_orcamento(os_selecionada)

    elif os_selecionada.status == "Aprovado":
        print("Atribuir técnico:")
        for i, tecnico in enumerate(lista_tecnicos, 1):
            print(f"{i} - {tecnico.nome} ({tecnico.especialidade})")
        
        try:
            escolha_tecnico = int(input("Escolha o técnico: ")) - 1
            os_selecionada.tecnico_responsavel = lista_tecnicos[escolha_tecnico].nome
            
            # Nova lógica para verificar se precisa de peças
            precisa_pecas = any("Troca de Peças" in s for s in os_selecionada.servicos_solicitados)
            if precisa_pecas:
                os_selecionada.status = "Aguardando peça"
                print(f"OS atribuída a {os_selecionada.tecnico_responsavel}. Status: Aguardando peça.")
            else:
                os_selecionada.status = "Em manutenção"
                print(f"OS atribuída a {os_selecionada.tecnico_responsavel}. Status: Em manutenção.")

        except (ValueError, IndexError):
            print("Opção de técnico inválida.")

    elif os_selecionada.status == "Aguardando peça":
        print("Peça chegou?")
        chegou = input("A peça chegou para a manutenção? (s/n): ").lower()
        if chegou == 's':
            os_selecionada.status = "Em manutenção"
            print("Status atualizado para 'Em manutenção'.")
        else:
            print("Continuando aguardando a peça.")

    elif os_selecionada.status == "Em manutenção":
        print("O serviço foi concluído? (s/n)")
        concluido = input().lower()
        if concluido == 's':
            os_selecionada.status = "Testando"
            print("Serviço concluído. Status: Testando.")
        else:
            print("A manutenção continua em andamento.")

    elif os_selecionada.status == "Testando":
        print("Os testes foram aprovados? (s/n)")
        aprovado = input().lower()
        if aprovado == 's':
            os_selecionada.status = "Pronto para retirar"
            os_selecionada.data_conclusao = datetime.now()
            print("Testes aprovados. Status: Pronto para retirar.")
        else:
            print("Teste não aprovado. Voltando para manutenção.")
            os_selecionada.status = "Em manutenção"

    elif os_selecionada.status == "Pronto para retirar":
        dias_armazenamento = (datetime.now() - os_selecionada.data_conclusao).days
        if dias_armazenamento > 30:
            taxa_extra = (dias_armazenamento - 30) * taxa_armazenamento_diaria
            print(f"ATENÇÃO: Cobrar taxa de armazenamento de R${taxa_extra:.2f} (passou {dias_armazenamento - 30} dias do prazo).")
            os_selecionada.valor_total += taxa_extra
            print(f"Novo valor total: R${os_selecionada.valor_total:.2f}")
        
        retirar = input("O cliente retirou o equipamento? (s/n): ").lower()
        if retirar == 's':
            os_selecionada.status = "Retirado"
            print("Equipamento entregue. Ordem de serviço finalizada.")
            tecnico_obj = next((t for t in lista_tecnicos if t.nome == os_selecionada.tecnico_responsavel), None)
            if tecnico_obj:
                tecnico_obj.produtividade += 1
    
    else:
        print("Esta OS já foi finalizada ou aguarda ações.")

def gerenciar_estoque():
    print("\n--- Gerenciamento de Estoque ---")
    for i, item in enumerate(estoque, 1):
        print(f"{i} - {item.nome} | Quantidade: {item.quantidade} | Preço de Custo: R${item.preco_custo:.2f}")
        if item.quantidade < 3:
            print("  ⚠ ESTOQUE BAIXO! Precisa comprar mais.")
    
    adicionar = input("\nDeseja adicionar um novo item ao estoque? (s/n): ").lower()
    if adicionar == 's':
        nome = input("Nome do item: ")
        try:
            quantidade = int(input("Quantidade: "))
            custo = float(input("Preço de custo: "))
            novo_item = ItemEstoque(nome, quantidade, custo)
            estoque.append(novo_item)
            print("Item adicionado com sucesso.")
        except ValueError:
            print("Entrada inválida. Quantidade e custo devem ser números.")

def relatorios():
    print("\n--- Relatórios ---")
    
    # Relatório 1: Vendas no mês
    vendas_mes = sum(os.valor_total for os in ordens_de_servico if os.status == "Retirado")
    print(f"1. Total de vendas no mês: R${vendas_mes:.2f}")
    
    # Relatório 2: Principais defeitos
    falhas_comuns = {}
    for os in ordens_de_servico:
        if os.problema in falhas_comuns:
            falhas_comuns[os.problema] += 1
        else:
            falhas_comuns[os.problema] = 1
    
    if falhas_comuns:
        print("\n2. Principais defeitos:")
        sorted_falhas = sorted(falhas_comuns.items(), key=lambda item: item[1], reverse=True)
        for problema, count in sorted_falhas:
            print(f"   - {problema}: {count} ocorrências")
    else:
        print("\n2. Não há dados de defeitos para exibir.")

    # Relatório 3: Produtividade do técnico
    if lista_tecnicos:
        tecnico_mais_produtivo = max(lista_tecnicos, key=lambda t: t.produtividade)
        print(f"\n3. Técnico mais produtivo: {tecnico_mais_produtivo.nome} (com {tecnico_mais_produtivo.produtividade} serviços concluídos)")
    else:
        print("\n3. Não há técnicos cadastrados.")
        
    # Relatório 4: Tempo médio de reparo
    tempos_reparo = []
    for os in ordens_de_servico:
        if os.status == "Retirado" and os.data_conclusao:
            tempo = os.data_conclusao - os.data_entrada
            tempos_reparo.append(tempo.total_seconds())

    if tempos_reparo:
        tempo_medio_segundos = sum(tempos_reparo) / len(tempos_reparo)
        tempo_medio = str(timedelta(seconds=tempo_medio_segundos)).split('.')[0]
        print(f"\n4. Tempo médio de reparo: {tempo_medio}")
    else:
        print("\n4. Não há dados suficientes para calcular o tempo médio de reparo.")

def menu():
    print("\n--- Sistema de Gestão TechFix ---")
    print("1 - Criar Ordem de Serviço")
    print("2 - Gerenciar Ordem de Serviço")
    print("3 - Gerenciar Estoque")
    print("4 - Ver Relatórios")
    print("5 - Sair")
    return input("\nEscolha uma opção: ")

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            criar_ordem_servico()
        elif opcao == '2':
            gerenciar_os()
        elif opcao == '3':
            gerenciar_estoque()
        elif opcao == '4':
            relatorios()
        elif opcao == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
