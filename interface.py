from os import system as sy
from time import sleep as sl
class gui():
    
    def __init__(self):
        sy("cls")
        self.opcao = 0    
    
    def inicio(self):
        self.processar_Escolha(self.gui_Inicio()) 
          
    def gui_Inicio(self):
        print("Seja bem vindo ao gerador de números")
        sl(1.5)
        sy("cls")
        sl(0.5)
        print("Aqui você pode gerar CPFs, RGs e mais...")
        sl(2)
        sy("cls")
        sl(0.5)
        print("Abrindo GUI...")
        sl(1)
        sy("cls")
        sl(0.5)
        print("- - - - - GERADOR DE NÚMEROS - - - - -\n\n")
        print("GERAR CPF [1]\nSAIR [2]\n\n")
        return str(input("Escolha uma opção: "))
           
    def processar_Escolha(self, opcao):
        match opcao:
            case "1":
                from gerador_cpf import gerador_CPF
                gerador_cpf = gerador_CPF()
                gerador_cpf.inicio()
            case "2":
                sy("cls")
                sl(0.5)
                print("Obrigado por visualizar meu projeto ;)")
                sl(2)
                sy("cls")
                sl(1)
                print("Encerando o programa...")
                sl(1.5)
                sy("cls")
                sl(1)
                exit()
            case _:
                sy("cls")
                sl(0.5)
                print("A opção está invalida. Selecione suas opções novamente")
                sl(1.5)
                sy("cls")
                sl(0.5)
                print("Iniciando o programa novamente...")
                sl(1)
                sy("cls")
                sl(1)
                self.inicio()
    
interface = gui()
interface.inicio()