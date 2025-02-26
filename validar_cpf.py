import general_functions as gf
class Validar_CPF():
    
    def inicio(self, exibir_inicio):
        self.CPF = []
        if exibir_inicio:
            self.mostrar_CPF(self.validar_CPF(self.verificar_Input(self.input())))
        self.processar_Opcao(self.carregar_Opcao())
            
    def input(self):
        gf.delay(0.5, 1)
        return str(input("Digite o CPF que deseja verificar: ")).strip()

    def verificar_Input(self, CPF_Usuario):
        if CPF_Usuario.isdigit() and len(CPF_Usuario) == 11:
            self.CPF = list(map(int, (CPF_Usuario)))
            return True
        return False

    def validar_CPF(self, numero_Valido):
        if numero_Valido:
            if gf.modulo_11(9, 10, self.CPF) == self.CPF[9] and gf.modulo_11(10, 11, self.CPF) == self.CPF[10]:
                return True
            return False
        gf.delay(0, 0.5)
        print("Valor incorreto. Coloque o CPPF sem pontos nem hífens")
        gf.delay(1.5, 0.5)
        self.inicio(True)
        
    def mostrar_CPF(self, CPF_Correto):
        if CPF_Correto:
            print("O CPF está correto, ele é um CPF válido")
        else:
            print("O CPF não é válido")

    def carregar_Opcao(self): #carrega a opção
        print("\nO que deseja fazer agora?\n")
        print("VERIFICAR NOVO CPF [1]\nVOLTAR [2]\n\n")
        return str(input("Escolha uma opção: "))
            
    def processar_Opcao(self, opcao): #processa a opção
        match opcao:
            case "1": #verifica outro CPF
                self.inicio(True)
            case "2": #volta para a tela de geração
                from validar_numero import Validar_Numero
                gf.delay(0, 0.5)
                Validar_Numero = Validar_Numero()
                Validar_Numero.inicio(False)
            case _: #volta para a tela de escolha
                gf.Opcao_Invalida()
                self.inicio(False)