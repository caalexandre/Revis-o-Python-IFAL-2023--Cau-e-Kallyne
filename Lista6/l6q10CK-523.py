#Lista de Exercício 6 - Questão 10
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

numeros_ate_dezenove = [
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"
]
        
dezenas = [
    "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"
]
        

class Numero:
    def __init__(self, numero):
        self._numero = numero

    def numero_por_extenso(self):

        if self._numero < 20:
            return numeros_ate_dezenove[self._numero]
        else:
            unidade = self._numero % 10
            dezena = self._numero // 10
            if unidade == 0:
                return dezenas[dezena]
            else:
                return dezenas[dezena] + " e " + numeros_ate_dezenove[unidade]


try:
    n = int(input("Digite um número até 99: "))

    if n < 0 or n > 99:
            print("Número inválido. Digite um número até 99.")
    else:
        numero_extenso = Numero(n).numero_por_extenso()
        print("Número por extenso:", numero_extenso)

except:
    print("Error")