import general_functions as gf
class gerador_CPF():
    
    def inicio(self, gerar_Novamente):
        if gerar_Novamente:
            self.CPF = []
            gf.carregamento("Gerando CPF...")
            self.gerar_Cpf()
            self.mostrar_CPF()
            self.processar_Opcao(self.carregar_Opcao())
        else:
            self.processar_Opcao(self.carregar_Opcao())
        
    def gerar_Cpf(self):
        for i in range(0, 9):
            self.CPF.append(gf.gerar_Numeros_Aleatorios(0, 9))
        self.CPF.append(self.gerar_validador(0, 9, 10, 0))
        self.CPF.append(self.gerar_validador(0, 10, 11, 0))           
    
    def gerar_validador(self, contador1, contador2, contador3, soma):
        while contador1 < contador2:
            soma += self.CPF[contador1] * contador3
            contador3 -= 1
            contador1 += 1
        if soma % 11 == 0 or soma % 11 == 1:
            return 0
        else:
            return 11 - (soma % 11)
        
    def mostrar_CPF(self):
        global CPF
        gf.delay(0, 0.5)
        print("CPF gerado com sucesso!!!")
        gf.delay(2, 1)
        self.CPF = "".join(map(str, self.CPF))
        print(f"Aqui está o seu CPF: {self.CPF[:3]}.{self.CPF[3:6]}.{self.CPF[6:9]}-{self.CPF[9:]}")
        
    def carregar_Opcao(self):
        print("\nO que deseja fazer agora?\n")
        print("GERAR NOVO CPF [1]\nVOLTAR [2]\n\n")
        return str(input("Escolha uma opção: "))
        
    def processar_Opcao(self, opcao):
        match opcao:
            case "1":
                self.inicio(True)
            case "2":
                from home import home
                gf.delay(0, 0.5)
                home = home()
                home.inicio(False)
            case _:
                gf.Opcao_Invalida()
                self.inicio(False)
        