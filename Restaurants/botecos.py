import sys
#sys.path.append('/home/vitorm/uneb_ws/2019-2/ED2/Grafos-Linux')
import Restaurants.btree_creator as btree
import Restaurants.key_insert as funcoes_bt
import Graphs.digrafo as digrafo
import networkx as graph
import System.sistema as sis

#Classe Restaurantes
class Boteco:
    def __init__(self, nome, dir_arquivo):
        self.nome = nome
        self.dir_arquivo = dir_arquivo
        self.Criar_Cardapio()
    
    def GetNome(self):
        return self.nome
    
    def GetTree(self):
        return self.cardapio

    def Criar_Cardapio(self):
        self.cardapio = btree.btree_creator('name',self.dir_arquivo)
        return self.cardapio

    def Imprimir_Cardapio(self):
        print((sis.color.BOLD + sis.color.BLUE + '-------- CARDAPIO DO ' + self.nome + ' --------' + sis.color.END).center(150))
        self.cardapio.seq_press(self.cardapio.root)
    
    def Controlar_Estoque(self,produto,qntd_produto):
        id_produto = self.cardapio.search_bt(self.cardapio.root, produto)
        funcoes_bt.decrease_stock(id_produto,self.dir_arquivo,qntd_produto)
        return True

'''
Os objetos serão salvos num dicionario "RegistroBotecos" na forma
{"boteco.name":boteco,}

Ao se instanciar um objeto do tipo boteco, deve-se adiciona-lo ao 
nós do grafo, e criar suas conexões
'''

#Funções de validação para os Restaurantes
def Cadastrar_Boteco(grafo, pontos_conexao):
    nome = (input("Digite o nome do estabelecimento: ")).upper()
    sis.LimparTerminal()
    if grafo.has_node(nome) == True:
        print("Já existe um estabelecimento cadastrado com esse nome")
        return False

    dir_arquivo = 'Grafos/Restaurants/Menus/' + input("Digite o nome do arquivo cardapio: ") + '.csv'
    #Criando objeto do tipo boteco -> contendo informações dos restaurantes
    novo_boteco = Boteco(nome, dir_arquivo)
    #Adcionando o novo boteco ao grafo, criando suas conexões simultaneamente
    grafo.add_node(novo_boteco.GetNome(), color='cyan')
    digrafo.Criar_Conexoes_Aleatorias(grafo, novo_boteco.GetNome(), pontos_conexao)
    return {nome: novo_boteco}
    
