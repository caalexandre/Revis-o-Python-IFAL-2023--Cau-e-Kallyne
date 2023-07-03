#Lista de Exercício 2 - Questão 4
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

class VerificadorLetra:
    def __init__(self):
        self.letra = ''
    def solicitar_letra(self):
        while True:
            try:
                self.letra = input("Digite uma letra: ").lower()
                if len(self.letra) != 1 or not self.letra.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Entrada inválida. Digite apenas uma letra.")
    def verificar_vogal_consoante(self):
        if self.letra in 'aeiou':
            return "A letra é uma vogal."
        else:
            return "A letra é uma consoante."
    def executar(self):
        self.solicitar_letra()
        resultado = self.verificar_vogal_consoante()
        print(resultado)
verificador = VerificadorLetra()
verificador.executar()
