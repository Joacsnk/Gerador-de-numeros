#sessão para geradores de números
import general_functions as gf #defs gerais
class Gerar_Numero():

    def inicio(self, exibir_inicio): #exibe painel de inicio ou não
        if exibir_inicio:
            self.Painel_Inicializacao()
        self.Processar_Escolha(self.Painel_Escolha())
    
    def Painel_Inicializacao(self): #exibe painel
        gf.delay(0, 0.5)
        print("Abrindo geradores...")
        gf.delay(1, 0.5)
    
    def Painel_Escolha(self): #exibe interface de escolha
        print("- - - - - GERADOR DE NÚMEROS - - - - -\n\n")
        print("GERAR CPF [1]\nVOLTAR [2]\n\n")
        return str(input("Escolha uma opção: "))
    
    def Processar_Escolha(self, opcao): #processa sua escolha
        match opcao:
            case "2": #retorna para o inicio principal
                from home import home 
                gf.delay(0, 0.5)
                hm = home()
                hm.inicio(False)
            case _: 
                gf.Opcao_Invalida(self) #indica opção inválida
                self.inicio(False)