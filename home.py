from os import system as sy
from time import sleep as sl
import gerenal_functions as gf
class home():
    
    def __init__(self):
        sy("cls")
    
    def inicio(self, exibir_inicio):
        if exibir_inicio == True:  
            self.Painel_Inicializacao()
        self.Processar_Escolha(self.Painel_Escolha())
    
    def Painel_Inicializacao(self):
        print("Seja bem vindo ao gerador de números")
        gf.delay(2, 0.5)
        print("Aqui você pode gerar CPFs, RGs e mais...")
        gf.delay(2, 0.5)
        print("Abrindo GUI...")
        gf.delay(1, 0.5)
    
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
            case "2":
                from validar_numero import Validar_Numero
                Validar_Numero = Validar_Numero()
                Validar_Numero.inicio(True)
            case "3":
                gf.delay(0, 0.5)
                print("Obrigado por visualizar meu projeto ;)")
                gf.delay(2, 1)
                print("Encerando o programa...")
                gf.delay(1.5, 1)
                exit()
            case _:
                gf.Opcao_Invalida(self)
                self.inicio(False)
    
if __name__ == "__main__":
    home = home()
    home.inicio(True)