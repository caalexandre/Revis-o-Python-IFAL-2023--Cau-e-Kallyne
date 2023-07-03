#Lista de Exercício 2 - Questão 19
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#19.Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


class DecomporNumero:
    def __init__(self):
        self.numero = 0
    def ler_numero(self):
        while True:
            try:
                self.numero = int(input("Digite um número inteiro menor que 1000: "))
                if self.numero < 1 or self.numero >= 1000:
                    raise ValueError
                break
            except ValueError:
                print("Número inválido. Digite um número inteiro menor que 1000.")
    def decompor(self):
        centenas = self.numero // 100
        dezenas = (self.numero % 100) // 10
        unidades = (self.numero % 100) % 10
        return centenas, dezenas, unidades
    def exibir_resultado(self, centenas, dezenas, unidades):
        resultado = []
        if centenas > 0:
            if centenas == 1:
                resultado.append("1 centena")
            else:
                resultado.append("{} centenas".format(centenas))
        if dezenas > 0:
            if dezenas == 1:
                resultado.append("1 dezena")
            else:
                resultado.append("{} dezenas".format(dezenas))
        if unidades > 0:
            if unidades == 1:
                resultado.append("1 unidade")
            else:
                resultado.append("{} unidades".format(unidades))
        print("{} = {}".format(self.numero, ", ".join(resultado)))
    def decompor_numero(self):
        self.ler_numero()
        centenas, dezenas, unidades = self.decompor()
        self.exibir_resultado(centenas, dezenas, unidades)
def main():
    numero = DecomporNumero()
    numero.decompor_numero()
if __name__ == "__main__":
    main()
