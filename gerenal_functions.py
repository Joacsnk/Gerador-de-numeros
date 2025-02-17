from os import system as sy
from time import sleep as sl

def delay(delay_inicio, delay_fim):
    sl(delay_inicio)
    sy("cls")
    sl(delay_fim)