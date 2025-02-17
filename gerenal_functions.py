from os import system as sy
from time import sleep as sl

def delay(delay_inicio, delay_fim):
    sl(delay_inicio)
    sy("cls")
    sl(delay_fim)

def Opcao_Invalida(self):
    delay(0, 0.5)
    print("A opção está invalida. Selecione suas opções novamente")
    delay(1.5, 0.5)