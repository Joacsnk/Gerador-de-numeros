#py para repetir defs
from os import system as sy #para limpar o terminal
from time import sleep as sl #para dar delay (UX)

def delay(delay_inicio, delay_fim): #delay de tempo e limpeza de código
    sl(delay_inicio)
    sy("cls")
    sl(delay_fim)

def Opcao_Invalida(): #mensagem de opção inválida
    delay(0, 0.5)
    print("A opção está invalida. Selecione suas opções novamente")
    delay(1.5, 0.5)
    
def carregamento(mensagem): #carrega mensagens de números completos
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

def modulo_11(contador1, ):
    contador_Nativo, soma = 0
    while contador_Nativo < contador1:
        soma += self.CPF[contador1] * contador3
        contador3 -= 1
        contador1 += 1
    if soma % 11 == 0 or soma % 11 == 1:
        return 0
    else:
        return 11 - (soma % 11)
    
def gerar_Numeros_Aleatorios(contador1, contador2): #gerador de números aleatórios
        from random import randint as ra
        return ra(contador1, contador2)