import sys
import Graphs.digrafo as digrafo
import Users.hasher as banco_dados
import Graphs.digrafo as digrafo
import networkx as graph
import System.sistema as sis

#Classe Usuarios
class Usuario:
    def __init__(self, email, senha, nome):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.Registrar()
    
    def GetNome(self):
        return self.nome
    
    def Registrar(self):
        banco_dados.InsertReg(self.email, self.senha, self.nome)
        banco_dados.WriteLog()
        return True

    

    

def Cadastrar_Cliente(grafo):
    email = input('Informe email do usuario: ')
    senha = input('Informe senha do usuario: ')
    nome = input('Informe nome do usuario: ')
    sis.LimparTerminal()
    if (grafo.has_node(nome) == True):
        print("Já existe um usuario cadastrado com esse nome")
        return False
    #Criando objeto do tipo Usuario -> contendo informações dos usuarios
    novo_usuario = Usuario(email, senha, nome)
    grafo.add_node(novo_usuario.GetNome(), color='cyan')
    digrafo.Criar_Conexao(grafo, grafo.graph['name'], novo_usuario.GetNome())
    return novo_usuario

def Login_Client(grafo):
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    sis.LimparTerminal()

    while banco_dados.Authentication(email, senha) == False:
        print("Senha ou E-Mail incorretos!\nTente novamente ou realize o cadastro")
        opcao = input("Digite 'Logar' para tentar novamente | 'Cadastrar' para se cadastrar\n\n--> ")
        if opcao.upper() == 'CADASTRAR':
            sis.LimparTerminal()
            Cadastrar_Cliente(grafo)
        else:
            sis.LimparTerminal()
            email = input('Digite seu email: ')
            senha = input('Digite sua senha:')
    
    #retorne o nome do cliente registrado que corresponde ao destinatario do pedido
    return banco_dados.GetByReg(email, senha)
