from os import system as sy
from time import sleep as sl
from gerenal_functions import delay as dl
class Gerar_Numero():

    def inicio(self, exibir_inicio):
        if exibir_inicio:
            self.Painel_Inicializacao()
        self.Processar_Escolha(self.Painel_Escolha())
    
    def Painel_Inicializacao(self):
        dl(0, 0.5)
        print("Abrindo geradores...")
        dl(1, 0.5)
    
    def Painel_Escolha(self):
        print("- - - - - GERADOR DE NÚMEROS - - - - -\n\n")
        print("GERAR CPF [1]\nVOLTAR [2]\n\n")
        return str(input("Escolha uma opção: "))
    
    def Processar_Escolha(self, opcao):
        match opcao:
            case "2":
                from home import home 
                dl(0, 0.5)
                hm = home()
                hm.inicio(False)
            case _:
                dl(0, 0.5)
                print("A opção está invalida. Selecione suas opções novamente")
                dl(1.5, 0.5)
                self.inicio(False)