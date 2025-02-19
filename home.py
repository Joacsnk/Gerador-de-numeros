#inicio princial
import general_functions as gf #def gerais
class home(): #classe principal
    
    def inicio(self, exibir_inicio): #inicia com ou sem o painel de inicio, dependendo do retorno
        gf.delay(0, 0)
        if exibir_inicio == True:  #sa bool como parâmetro para iniciar com ou sem painel
            self.Painel_Inicializacao()
        self.Processar_Escolha(self.Painel_Escolha())
    
    def Painel_Inicializacao(self): #inicio estilo carregamento
        print("Seja bem vindo ao gerador de números")
        gf.delay(2, 0.5)
        print("Aqui você pode gerar CPFs, RGs e mais...")
        gf.delay(2, 0.5)
        print("Abrindo GUI...")
        gf.delay(1, 0.5)
    
    def Painel_Escolha(self): #painel para selecionar opções
        print("- - - - - GERADOR DE NÚMEROS - - - - -\n\n")
        print("GERAR NÚMERO [1]\nVERFICAR NÚMERO [2]\nSAIR [3]\n\n")
        return str(input("Escolha uma opção: "))
           
    def Processar_Escolha(self, opcao): #processa o caminho de cada opção
        match opcao:
            case "1": #irá para o menu de geração
                from gerar_numero import Gerar_Numero
                Gerar_Numero = Gerar_Numero()
                Gerar_Numero.inicio(True)
            case "2": #irá para o menu de validação
                from validar_numero import Validar_Numero
                Validar_Numero = Validar_Numero()
                Validar_Numero.inicio(True)
            case "3": #desligando o programa
                gf.delay(0, 0.5)
                print("Obrigado por visualizar meu projeto ;)")
                gf.delay(2, 1)
                print("Encerando o programa...")
                gf.delay(1.5, 1)
                exit()
            case _: #repetindo o inicio sem o painel inicial
                gf.Opcao_Invalida(self)
                self.inicio(False)
    
if __name__ == "__main__": #confirmação para o código rodar inicialmente nesse arquivo
    home = home()
    home.inicio(True)  