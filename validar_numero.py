#sessão de validadores de números
import general_functions as gf #fnções gerais
class Validar_Numero():

    def inicio(self, exibir_inicio): #exibir ou não o painel de inicio
        if exibir_inicio:
            self.Painel_Inicializacao()
        self.Processar_Escolha(self.Painel_Escolha())
    
    def Painel_Inicializacao(self): #painel de inicio
        gf.delay(0, 0.5)
        print("Carregando validações...")
        gf.delay(1, 0.5)
    
    def Painel_Escolha(self): #escolha e opções
        print("- - - - - GERADOR DE NÚMEROS - - - - -\n\n")
        print("VALIDAR CPF [1]\nVOLTAR [2]\n\n")
        return str(input("Escolha uma opção: "))
    
    def Processar_Escolha(self, opcao): #processando sua escolha
        match opcao:
            case "2": #leva novamente para o inicio principal
                from home import home 
                gf.delay(0, 0.5)
                hm = home()
                hm.inicio(False)
            case _:
                gf.Opcao_Invalida(self) #indica opção inválida
                self.inicio(False)