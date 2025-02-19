#py para repetir defs
from os import system as sy #para limpar o terminal
from time import sleep as sl #para dar delay (UX)

def delay(delay_inicio, delay_fim): #delay de tempo e limpeza de código
    sl(delay_inicio)
    sy("cls")
    sl(delay_fim)

def Opcao_Invalida(self): #mensagem de opção inválida
    delay(0, 0.5)
    print("A opção está invalida. Selecione suas opções novamente")
    delay(1.5, 0.5)
    
def carregamento(mensagem):
    sy("cls")
    sl(1)
    print(mensagem)
    sl(0.5)
    print(".")
    sl(0.5)
    print(".")
    sl(0.5)
    print(".")
    sl(0.5)
    print(".")
    sl(0.5)
    print(".")
    
def gerar_Numeros_Aleatorios(contador1, contador2):
        from random import randint as ra
        return ra(contador1, contador2)