from os import system as sy
from time import sleep as sl
import gerenal_functions as gf
class Validar_Numero():

    def inicio(self, exibir_inicio):
        if exibir_inicio:
            self.Painel_Inicializacao()
        self.Processar_Escolha(self.Painel_Escolha())
    
    def Painel_Inicializacao(self):
        gf.delay(0, 0.5)
        print("Carregando validações...")
        gf.delay(1, 0.5)
    
    def Painel_Escolha(self):
        print("- - - - - GERADOR DE NÚMEROS - - - - -\n\n")
        print("VALIDAR CPF [1]\nVOLTAR [2]\n\n")
        return str(input("Escolha uma opção: "))
    
    def Processar_Escolha(self, opcao):
        match opcao:
            case "2":
                from home import home 
                gf.delay(0, 0.5)
                hm = home()
                hm.inicio(False)
            case _:
                gf.Opcao_Invalida(self)
                self.inicio(False)