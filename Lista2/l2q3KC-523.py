#Lista de Exercício 2 - Questão 3
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.



class VerificadorGenero:
    def __init__(self):
        self.letra = ''

    def solicitar_letra(self):
        while True:
            try:
                self.letra = input("Digite uma letra (F ou M): ")
                if self.letra.upper() not in ['F', 'M']:
                    raise ValueError
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas F ou M.")

    def verificar_genero(self):
        if self.letra.upper() == 'F':
            return "F - Feminino"
        elif self.letra.upper() == 'M':
            return "M - Masculino"
        else:
            return "Sexo Inválido."

    def executar(self):
        self.solicitar_letra()
        resultado = self.verificar_genero()
        print(resultado)
verificador = VerificadorGenero()
verificador.executar()

