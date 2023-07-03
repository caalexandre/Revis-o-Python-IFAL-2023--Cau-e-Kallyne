#Lista de Exercício 2 - Questão 24
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#24.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma #frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.


class OperacoesNumeros:
    def ler_numeros(self):
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Valores inválidos. Digite números.")
        return num1, num2
    def selecionar_operacao(self):
        print("Selecione a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        while True:
            try:
                opcao = int(input("Opção: "))
                if opcao in [1, 2, 3, 4]:
                    break
                else:
                    print("Opção inválida. Digite novamente.")
            except ValueError:
                print("Opção inválida. Digite novamente.")
        return opcao
    def executar(self):
        num1, num2 = self.ler_numeros()
        operacao = self.selecionar_operacao()
        if operacao == 1:
            resultado = num1 + num2
            operacao_str = "Soma"
        elif operacao == 2:
            resultado = num1 - num2
            operacao_str = "Subtração"
        elif operacao == 3:
            resultado = num1 * num2
            operacao_str = "Multiplicação"
        else:
            resultado = num1 / num2
            operacao_str = "Divisão"
        print(f"Resultado da {operacao_str}: {resultado}")
        self.verificar_par_impar(resultado)
        self.verificar_positivo_negativo(resultado)
        self.verificar_inteiro_decimal(resultado)
    def verificar_par_impar(self, numero):
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")
    def verificar_positivo_negativo(self, numero):
        if numero > 0:
            print("O número é positivo.")
        elif numero < 0:
            print("O número é negativo.")
        else:
            print("O número é zero.")
    def verificar_inteiro_decimal(self, numero):
        if numero == round(numero):
            print("O número é inteiro.")
        else:
            print("O número é decimal.")
operacoes = OperacoesNumeros()
operacoes.executar()
