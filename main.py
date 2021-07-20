
import sys
import System.sistema as sis
import Graphs.digrafo as digrafo
import Restaurants.botecos as botecos
import Users.usuarios as usuario

#Programa principal - Menus
def Cadastros(grafo):
    restaurantes = {}
    mapa = grafo.GetMapa()

    while True:
    #Cadastro de grafo, estabelecimentos e clientes
        sis.LimparTerminal()
        print(sis.color.BOLD + sis.color.BLUE + "Menu de cadastro de usuarios, estabelecimentos e clientes" + sis.color.END)
        print("Digite 'Usuario' para cadastrar usuarios | ...")
        print("Digite 'Boteco' para cadastrar botecos | ...")
        opcao = (input("Digite 'Sair' para sair do menu | ...\n\n--> ")).upper()
        sis.LimparTerminal()
        
        if opcao == 'BOTECO':
            centros_intermed = grafo.GetCentros_Intermed()
            novo_boteco = botecos.Cadastrar_Boteco(mapa, centros_intermed)
            restaurantes.update(novo_boteco)
        elif opcao == 'USUARIO':
            usuario.Cadastrar_Cliente(mapa)
        else:
            return restaurantes

def Visualizar_Cardapios(restaurantes, grafo):
    mapa = grafo.GetMapa()
    #O cliente deve se identificar antes de visualizar o cardapio
    cliente = usuario.Login_Client(mapa)
    #Impressao de menus dos restaurantes
    #print(restaurantes)
    while True:
        sis.LimparTerminal()
        print(sis.color.BOLD + sis.color.BLUE + "Menu de cardapios dos botecos cadastrados".center(150) + sis.color.END)
        for nome_boteco in restaurantes.keys():
            print(nome_boteco)
        print('Digite o nome do boteco que deseja visualizar o menu | ...')
        opcao = (input("Digite 'Sair' para sair do menu | ...\n\n--> ")).upper()
        sis.LimparTerminal()

        if opcao == 'SAIR':
            return 0

        else:
            menu = restaurantes[opcao]
            menu.Criar_Cardapio()
            menu.Imprimir_Cardapio()

            print("\nDigite 'Pedir' para realizar um pedido | ...")
            opcao = (input("Digite 'Voltar' para retornar ao menu anterior | ...\n\n--> ")).upper()
            if opcao == 'PEDIR':
                fornecedores, info_produto = Gerar_Pedido(restaurantes)
                if fornecedores == {}:
                    print(sis.color.RED + "Produto nao encontrado em nenhum estabelecimento cadastrado!!!" + sis.color.END)
                    continue
                dijkstra = digrafo.Busca_Dijkstra(mapa,fornecedores,cliente)
                boteco = restaurantes[dijkstra]
                boteco.Controlar_Estoque(info_produto['produto'], info_produto['qntd'])
                grafo.Plotar_Grafo()
                
    return 1

def Gerar_Pedido(restaurantes):
    produto = (input("Digite o nome do produto selecionado: ")).upper()
    quantidade = int(input("Digite a quantidade do produto selecionado: "))

    fornecedores = {}
    for boteco_name, boteco in restaurantes.items():
        tree = boteco.GetTree()
        no = tree.search_node(tree.root, produto)
        if no != None and no[1] >= quantidade:
            fornecedores[boteco_name] = no

    return fornecedores, {'produto':produto,'qntd':quantidade}

def start():
    mapa = digrafo.Grafo()
    sis.LimparTerminal()
    print('\n\n')
    print(sis.color.BOLD + sis.color.RED + "Bem vindo ao sistema de distribuição de alimentos baseado em mapas direcionais de Dijkstra".center(150) + sis.color.END)
    restaurantes = Cadastros(mapa)
    sis.LimparTerminal()

    print("Digite 'Ver' para visualizar o menu ou realizar pedidos | ...")
    opcao = (input("Digite 'Sair' para sair do menu | ...\n\n--> ")).upper()
    sis.LimparTerminal()
    while opcao != 'Sair':
        print(sis.color.BOLD + sis.color.BLUE + "Visualização de cardapios e realização de pedidos".center(150) + sis.color.END)
        Visualizar_Cardapios(restaurantes,mapa)

start()
