#Lista de Exercício 3 - Questão 39
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

class Ficha:
    def calcular_altura():
        altura_maior = 0
        nome_maior = 0
        altura_menor = float('inf')
        nome_menor = 0
        try:
            for i in range(10):
                nome = input("Digite o nome do infeliz: ")
                altura = int(input("Digite a altura do infeliz: "))

                if altura > altura_maior:
                    altura_maior = altura
                    nome_maior = nome
                    
                if altura < altura_menor:
                    altura_menor = altura
                    nome_menor = nome
        except:
            print("Error")
        
        print(f"O maior aluno é {nome_maior}, com {altura_maior}cm de altura.")
        print(f"O menor aluno é {nome_menor}, com {altura_menor}cm de altura.")

Ficha.calcular_altura()