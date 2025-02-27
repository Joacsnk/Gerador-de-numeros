#py para repetir defs
from os import system as sy #para limpar o terminal
from time import sleep as sl #para dar delay (UX)

def delay(delay_inicio, delay_fim): #delay de tempo e limpeza de código
    sl(delay_inicio)
    sy("cls")
    sl(delay_fim)

def Opcao_Invalida(mensagem): #mensagem de opção inválida
    delay(0, 0.5)
    match mensagem:
       case 1: #opção inválida
          print("\33[31mA opção está invalida. Selecione suas opções novamente\33[m")
       case 2: #valor de CPF incorreto
          print("\33[31mValor incorreto. Coloque o CPF sem pontos, sem hífens e com 11 dígitos\33[m")
    delay(1.7, 0.5)
    
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
    sy("cls")

def painel_Escolha(mensagem_Up, painel): #painel para selecionar opções
        print(mensagem_Up, painel)
        return str(input("Escolha uma opção: "))

def modulo_11(contador1, contador2, CPF ):
    contador_Nativo = 0
    soma = 0
    while contador_Nativo < contador1:
        soma += CPF[contador_Nativo] * contador2
        contador2 -= 1
        contador_Nativo += 1
    if soma % 11 == 0 or soma % 11 == 1:
        return 0
    else:
        return 11 - (soma % 11)
    
def apresentacao_Inicio(n1, n2, mensagem , n3, n4):
        delay(n1, n2)
        print(mensagem)
        delay(n3, n4)

def gerar_Numeros_Aleatorios(contador1, contador2): #gerador de números aleatórios
        from random import randint as ra
        return ra(contador1, contador2)