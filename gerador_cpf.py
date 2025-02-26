#gerador de CPF
import general_functions as gf #dfs gerais
class gerador_CPF(): 
    
    def inicio(self, gerar_Novamente): #def principal / gera ou não outro CPF
        if gerar_Novamente:
            self.CPF = []
            gf.carregamento("Gerando CPF...") #carregar mensagem de produção
            self.gerar_Cpf()
            gf.delay(0, 0.5)
            print("CPF gerado com sucesso!!!")
        self.mostrar_CPF()
        self.processar_Opcao(self.carregar_Opcao())
        
    def gerar_Cpf(self): #gera o CPF
        for i in range(0, 9): #pega 9 números aleatórios
            self.CPF.append(gf.gerar_Numeros_Aleatorios(0, 9))
        self.CPF.append(gf.modulo_11(9, 10, self.CPF)) #faz o 10º número
        self.CPF.append(gf.modulo_11(10, 11, self.CPF))#faz o 11º número        
        
    def mostrar_CPF(self): #mostra o CPF em números
        gf.delay(0.5, 0.5)
        self.CPF = "".join(map(str, self.CPF))
        print(f"Aqui está o seu CPF: {self.CPF[:3]}.{self.CPF[3:6]}.{self.CPF[6:9]}-{self.CPF[9:]}")
        
    def carregar_Opcao(self): #carrega a opção
        print("\nO que deseja fazer agora?\n")
        print("GERAR NOVO CPF [1]\nVOLTAR [2]\n\n")
        return str(input("Escolha uma opção: "))
        
    def processar_Opcao(self, opcao): #processa a opção
        match opcao:
            case "1": #cria outro CPF
                self.inicio(True)
            case "2": #volta para a tela de geração
                from gerar_numero import Gerar_Numero
                gf.delay(0, 0.5)
                Gerar_Numero = Gerar_Numero()
                Gerar_Numero.inicio(False)
            case _: #volta para a tela de escolha
                gf.Opcao_Invalida()
                self.inicio(False)
        
