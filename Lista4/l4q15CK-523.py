#Lista de Exercício 4 - Questão 15
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

class Valores:
    def separacaoValor():
        try:
            valores_lidos = 0
            valores = []
            soma = 0
            acima = 0
            maior_sete = 0

            while True:
                valor = float(input("Digite um valor: "))

                if valor < 0:
                    break

                else:
                    valores_lidos += 1
                    valores.append(valor)

            print(valores)

            qtd = len(valores)

            for i in reversed(range(qtd)):
                print(valores[i])

            for valor in valores:
                soma += valor

            print(f"Soma de todos os valores: {soma}")

            media = (soma/qtd)

            print(f"Média dos valores: {media}")

            for valor in valores:
                if valor > media:
                    acima += 1
                
                if valor < 7:
                    maior_sete += 1

            print(f"Quantidade de valores a cima da média: {acima}")
            print(f"Quantidade de valores menor de 7: {maior_sete}")
        
        except:
            print("Error")

Valores.separacaoValor()