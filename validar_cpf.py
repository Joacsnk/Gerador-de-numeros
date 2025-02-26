import general_functions as gf
class Validar_CPF():
    
    def inicio(self, exibir_inicio):
        self.CPF = []
        if exibir_inicio:
            self.validar_CPF(self.verificar_Input(self.input()))
            
    def input(self):
        gf.delay(0.5, 1)
        return str(input("Digite o CPF que deseja verificar: ".strip()))

    def verificar_Input(self, CPF_Usuario):
        if CPF_Usuario.isdigit() and len(CPF_Usuario) == 11:
            self.CPF = map(int, (CPF_Usuario.split()))
            return True
        return False

    def validar_CPF(self, numero_Valido):
        if numero_Valido:
            print("aee")
            print(self.CPF)
            
            
            
            
            
Validar_CPF = Validar_CPF()
Validar_CPF.inicio(True)