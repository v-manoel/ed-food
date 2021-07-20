import sys
#sys.path.append('/home/vitorm/uneb_ws/2019-2/ED2/Grafos-Linux')
import System.sistema as sis
import networkx as graph
import matplotlib.pyplot as plt
from random import randint
import time

#Classe Grafos
class Grafo:
    def __init__(self, nome='EdFood', data='18 de feveiro de 20', cor='deepskyblue', qntd_pontos =6):
        self.mapa = graph.DiGraph(name=nome ,color=cor, date=data)
        self.centros_intermed = self.Criar_Pontos(qntd_pontos)

    def Criar_Pontos(self, qntd_pontos):
        centros_intermed = []
        nome_base = 'Centro'
        for sufixo in range(qntd_pontos):
            nome_centro = nome_base + str(sufixo)
            centros_intermed.append(nome_centro)
            #Inserindo os pontos no grafo
            self.mapa.add_node(nome_centro, color='darkturquoise')
            Criar_Conexao(self.mapa, nome_centro, self.mapa.graph['name'])
        return centros_intermed

    def GetCentros_Intermed(self):
        return self.centros_intermed
    
    def GetMapa(self):
        return self.mapa

    def Plotar_Grafo(self):
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0]=20
        fig_size[1]=10
        plt.rcParams["figure.figsize"]=fig_size

        layout =graph.circular_layout(self.mapa)
        edges = self.mapa.edges()
        colors_e = [self.mapa[i][j]['color'] for i,j in edges]
        labels = {edge: self.mapa.get_edge_data(edge[0], edge[1])["weight"] for edge in self.mapa.edges()}
        colors_n = [color for color in graph.get_node_attributes(self.mapa, 'color').values()]
        graph.draw_networkx_edge_labels(self.mapa, pos=layout, edge_labels=labels, font_color = 'black', font_size='12', font_family='arial', font_weight='bold')
        graph.draw(self.mapa, pos=layout, edgelist=edges, edge_color=colors_e, width=3.5, with_labels = True, font_weight='bold', font_size='14')
    
        return plt.show()


def Criar_Conexao(grafo, start_point, end_point, path_color ='black'):
    distance = randint(5,30)
    grafo.add_edge(start_point, end_point, weight = distance, color = path_color)

def Criar_Conexoes_Aleatorias(grafo,start_point,end_points, path_color='black'):
    n_points = len(end_points)
    for count in range(randint(1,n_points)):
        index = randint(1,n_points -1)
        Criar_Conexao(grafo,start_point,end_points[index])

def Recriar_Todas_Conexoes(grafo):
    for edge in grafo.edges():
        distance = randint(5,30)
        grafo[edge[0]][edge[1]]['weight'] = distance

def Busca_Dijkstra(grafo,start_points,end_point):
    dijkstra = {"distancia": None, "caminho": None}

    for point in start_points.keys():
        distancia, caminho = graph.bidirectional_dijkstra(grafo,point,end_point)
        print("Rota:", caminho, "  Distancia: ", distancia,'km')

        #Selecionando caminho mais curto
        if (dijkstra['distancia'] == None and dijkstra['caminho'] == None) or (dijkstra['distancia'] > distancia):
            dijkstra['distancia']= distancia
            dijkstra['caminho']= caminho
            boteco_nome = point
        #Grifando caminhos de mesmo tamanho
        if dijkstra['distancia'] == distancia:
            for node in range(len(dijkstra['caminho']) -1):
                grafo[dijkstra['caminho'][node]][dijkstra['caminho'][node + 1]]['color'] = 'orange'
    
    #Grifando o caominho mais curto
    sis.LimparTerminal()
    print("Caminho final selecionado!")
    print("Rota:", dijkstra['caminho'], "  Distancia: ", dijkstra['distancia'],'km')
    for node in range(len(dijkstra['caminho']) -1):
        grafo[dijkstra['caminho'][node]][dijkstra['caminho'][node + 1]]['color'] = 'red'
    
    return boteco_nome
    


