import general_functions as gf
class Validar_CPF():
    
    def inicio(self, exibir_inicio):
        gf.delay(0, 0.5)
        self.CPF = [] #define a var do CPF
        if exibir_inicio: #exibe ou não o início
            self.mostrar_CPF(self.validar_CPF(self.verificar_Input(self.input()))) #pegar, verificar, validar e mostrar
        self.processar_Opcao(gf.painel_Escolha("\33[33mO que deseja fazer agora?\n\n", "VERIFICAR NOVO CPF [1]   VOLTAR [2]\n\n")) #mostrar opções
            
    def input(self):
        return str(input("\33[33mDigite o CPF que deseja verificar: ")).strip() #pega o CPF

    def verificar_Input(self, CPF_Usuario): #verifica se está digitado corretamente e transforma em list e int 
        if CPF_Usuario.isdigit() and len(CPF_Usuario) == 11:
            self.CPF = list(map(int, (CPF_Usuario)))
            return True
        return False

    def validar_CPF(self, numero_Valido): #verificar CPF
        if numero_Valido:
            if gf.modulo_11(9, 10, self.CPF) == self.CPF[9] and gf.modulo_11(10, 11, self.CPF) == self.CPF[10]:
                return True
            return False
        gf.Opcao_Invalida(2)
        self.inicio(True)
        
    def mostrar_CPF(self, CPF_Correto): #mostrando o CPF
        gf.delay(0, 0.5)
        gf.carregamento("\33[33mVerificando CPF...")
        gf.delay(0, 0.5)    
        if CPF_Correto:
            print("\33[32mO CPF é válido! Os verificadores estão de acordo\33[33m\n")
        else:
            print("\33[31mO CPF não está validado corretamente. Os dígitos verificadores estão incorretos\33[33m\n\n")
            
    def processar_Opcao(self, opcao): #processa a opção
        match opcao:
            case "1": #verifica outro CPF
                gf.delay(0, 1)
                self.inicio(True)
            case "2": #volta para a tela de geração
                from validar_numero import Validar_Numero
                gf.delay(0, 0.5)
                Validar_Numero = Validar_Numero()
                Validar_Numero.inicio(False)
            case _: #volta para a tela de escolha
                gf.Opcao_Invalida(1)
                self.inicio(False)
                
Validar_CPf = Validar_CPF()
Validar_CPf.inicio(True)