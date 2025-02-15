from os import system as sy
from time import sleep as sl
CPF = 0
opcao = ""
class gerador_CPF():
    
    def inicio(self):
        self.CPF = []
        self.carregamento()
        self.gerar_Cpf()
        self.mostrar_CPF()
        self.carregar_Opcao()
        self.processar_Opcao()
        
    def inicio_caso_erro(self):
        self.carregar_Opcao()
        self.processar_Opcao()
        
    def carregamento(self):
        sy("cls")
        sl(1)
        print("Gerando o cpf...")
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
        
    def gerar_Cpf(self):
        self.redefinir_Variaveis()
        self.gerar_9_numeros()
        self.redefinir_Variaveis()
        self.CPF.append(self.gerar_10o(10, 9))
        self.redefinir_Variaveis()
        self.CPF.append(self.gerar_10o(11, 10))
        
    def redefinir_Variaveis(self):
        self.contador1 = 0
        self.contador2 = 0
        self.soma = 0
             
    def gerar_9_numeros(self):
        from random import randint as ra
        while self.contador1 < 9:
            self.CPF.append(ra(0, 9))
            self.contador1 += 1
    
    def gerar_10o(self, contador, contador2):
        while self.contador1 < contador2:
            self.soma += self.CPF[self.contador1] * contador
            contador -= 1
            self.contador1 += 1
        if self.soma % 11 == 0 or self.soma % 11 == 1:
            return 0
        else:
            return 11 - (self.soma % 11)
        
    def mostrar_CPF(self):
        global CPF
        sy("cls")
        print("CPF gerado com sucesso!!!")
        sl(2)
        sy("cls")
        sl(1)
        CPF = "".join(map(str, self.CPF))
        print(f"Aqui está o seu CPF: {CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}")
        sl(3)
        
    def carregar_Opcao(self):
        global opcao
        print("\nO que deseja fazer agora?\n")
        sl(1)
        print("GERAR NOVO CPF [1]\nVOLTAR [2]\n\n")
        opcao = str(input("Escolha uma opção: "))
        
    def processar_Opcao(self):
        global opcao
        match opcao:
            case "1":
                self.inicio()
            case "2":
                from interface import gui
                sy("cls")
                interface = gui()
                interface.inicio()
            case _:
                sy("cls")
                sl(0.5)
                print("A opção está invalida. Selecione suas opções novamente")
                sl(1.5)
                sy("cls")
                sl(0.5)
                self.inicio_caso_erro()
        