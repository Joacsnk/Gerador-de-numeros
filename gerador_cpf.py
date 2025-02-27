#gerador de CPF
import general_functions as gf 
class Gerador_CPF(): 
    
    def inicio(self, gerar_Novamente): #def principal
        if gerar_Novamente: #gera ou não outro CPF
            self.CPF = [] #define a var como null
            gf.carregamento("\33[33mGerando CPF...") #carregar mensagem de produção
            self.gerar_CPF() #gerar CPF
            gf.delay(0, 0.5)
            print("\33[32mCPF gerado com sucesso!!!\33[33m")
        self.mostrar_CPF() #mostrar o CPF
        self.processar_Opcao(gf.painel_Escolha("\n\33[33mO que deseja fazer agora?", "\n\nGERAR NOVO CPF [1]   VOLTAR [2]\n\n")) #opção
        
    def gerar_CPF(self): #gera o CPF
        for i in range(0, 9): #pega 9 números aleatórios
            self.CPF.append(gf.gerar_Numeros_Aleatorios(0, 9))
        self.CPF.append(gf.modulo_11(9, 10, self.CPF)) #faz o 10º número
        self.CPF.append(gf.modulo_11(10, 11, self.CPF))#faz o 11º número        
        
    def mostrar_CPF(self): #mostra o CPF em números
        gf.delay(0.5, 0.5)
        self.CPF = "".join(map(str, self.CPF))
        print(f"\33[33mAqui está o seu CPF: \33[32m{self.CPF[:3]}.{self.CPF[3:6]}.{self.CPF[6:9]}-{self.CPF[9:]}\33[33m")       
    
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
                gf.Opcao_Invalida(1)
                self.inicio(False)
        
