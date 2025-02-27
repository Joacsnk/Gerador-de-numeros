#inicio princial
import general_functions as gf #def gerais
class home(): #classe principal
    
    def inicio(self, exibir_inicio): #inicia com ou sem o painel de inicio, dependendo do retorno
        if exibir_inicio == True:  #inicia o painel
            gf.delay(0, 0.5) #limpando a tela
            gf.apresentacao_Inicio(0, 0, "\33[33mSeja bem vindo ao gerador de números\33", 1.7, 0.5,) #apresentação
        self.Processar_Escolha(gf.painel_Escolha("\33[33m≿————-　     GERADOR DE NÚMEROS     　————-≾\n\n", "GERAR NÚMERO [1]   VERFICAR NÚMERO [2]   SAIR [3]\n\n")) #escolha com parâmetro (texto visual para escolha)
           
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
                exit()
            case _: #repetindo o inicio sem o painel inicial
                gf.Opcao_Invalida(1)
                self.inicio(False)
    
if __name__ == "__main__": #confirmação para o código rodar inicialmente nesse arquivo
    home = home()
    home.inicio(True)  