from os import system as sy
from time import sleep as sl
from gerenal_functions import delay as dl
class home():
    
    def __init__(self):
        sy("cls")
    
    def inicio(self, exibir_inicio):
        if exibir_inicio == True:  
            self.Painel_Inicializacao()
        self.Processar_Escolha(self.Painel_Escolha())
    
    def Painel_Inicializacao(self):
        print("Seja bem vindo ao gerador de números")
        dl(2, 0.5)
        print("Aqui você pode gerar CPFs, RGs e mais...")
        dl(2, 0.5)
        print("Abrindo GUI...")
        dl(1, 0.5)
    
    def Painel_Escolha(self):
        print("- - - - - GERADOR DE NÚMEROS - - - - -\n\n")
        print("GERAR NÚMERO [1]\nVERFICAR NÚMERO [2]\nSAIR [3]\n\n")
        return str(input("Escolha uma opção: "))
           
    def Processar_Escolha(self, opcao):
        match opcao:
            case "1":
                from gerar_numero import Gerar_Numero
                Gerar_Numero = Gerar_Numero()
                Gerar_Numero.inicio(True)
            case "3":
                dl(0, 0.5)
                print("Obrigado por visualizar meu projeto ;)")
                dl(2, 1)
                print("Encerando o programa...")
                dl(1.5, 1)
                exit()
            case _:
                dl(0, 0.5)
                print("A opção está invalida. Selecione suas opções novamente")
                dl(1.5, 0.5)
                self.inicio(False)
    
if __name__ == "__main__":
    home = home()
    home.inicio(True)