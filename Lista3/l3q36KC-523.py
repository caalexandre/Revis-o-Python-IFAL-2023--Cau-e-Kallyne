#Lista de Exercício 3 - Questão 36
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#36.Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.


class Numero:
    def __init__(self, numero, inicio, fim):
        self.numero = numero
        self.inicio = inicio
        self.fim = fim

    def tabuada_personalizada(self):
        if fim < self.inicio:
            print("Erro: O valor final não pode ser menor que o valor inicial.")
            return

        print(f"Vou montar a tabuada de {self.numero} começando em {self.inicio} e terminando em {self.fim}:")
        for i in range(self.inicio, self.fim + 1):
            resultado = self.numero * i
            print(f"{self.numero} X {i} = {resultado}")
try:
    numero = int(input("Digite um número inteiro para a tabuada: "))
    inicio = int(input("Digite o valor inicial da tabuada: "))
    fim = int(input("Digite o valor final da tabuada: "))

    Numero(numero, inicio, fim).tabuada_personalizada()

except ValueError:
    print("Valor inválido. Digite um número inteiro válido.")
