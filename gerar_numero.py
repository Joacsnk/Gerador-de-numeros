#sessão para geradores de números
import general_functions as gf 
class Gerar_Numero():

    def inicio(self, exibir_inicio):
        if exibir_inicio:
            gf.apresentacao_Inicio(0, 0.5, "Abrindo geradores...", 1, 0.5)
        self.Processar_Escolha(gf.painel_Escolha("\33[33m━━━━━ ━ GERADOR ━ ━━━━━\n\n", "GERAR CPF [1]   VOLTAR [2]\n\n"))
    
    def Processar_Escolha(self, opcao): #processa sua escolha
        match opcao:
            case "1": #vai para o gerador de CPF
                gf.delay(0, 0.5)
                from gerador_cpf import Gerador_CPF
                Gerador_CPF = Gerador_CPF()
                Gerador_CPF.inicio(True)
            case "2": #retorna para o menu anterior
                from home import home 
                gf.delay(0, 0.5)
                home = home()
                home.inicio(False)
            case _: #opção errada
                gf.Opcao_Invalida(1)
                self.inicio(False)