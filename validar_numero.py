#sessão de validadores de números
import general_functions as gf 
class Validar_Numero():

    def inicio(self, exibir_inicio): 
        if exibir_inicio: #exibir ou não o painel de inicio
            gf.apresentacao_Inicio(0, 0.5, "\33[33mCarregando validações...", 1, 0.5)
        self.Processar_Escolha(gf.painel_Escolha("\33[33m━━━━━ ━ VALIDADOR ━ ━━━━━\n\n", "VALIDAR CPF [1]   VOLTAR [2]\n\n"))
    
    def Processar_Escolha(self, opcao): 
        match opcao:
            case "1":
                from validar_cpf import Validar_CPF
                gf.delay(0, 0.5)
                Validar_CPF = Validar_CPF()
                Validar_CPF.inicio(True)
            case "2": #leva novamente para o inicio principal
                from home import home 
                gf.delay(0, 0.5)
                home = home()
                home.inicio(False)
            case _:
                gf.Opcao_Invalida(1) #indica opção inválida
                self.inicio(False)