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
        self.CPF.append(self.gerar_validador(0, 9, 10, 0)) #faz o 10º número
        self.CPF.append(self.gerar_validador(0, 10, 11, 0))#faz o 11º número        
    
    def gerar_validador(self, contador1, contador2, contador3, soma): #faz a validação: (n1 * y) + (n2 * y-1) + (n3 * y-2) +...+ (n9 * y-8) = x
        while contador1 < contador2:
            soma += self.CPF[contador1] * contador3
            contador3 -= 1
            contador1 += 1
        if soma % 11 == 0 or soma % 11 == 1:
            return 0
        else:
            return 11 - (soma % 11)
        
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
        