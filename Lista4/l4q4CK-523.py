#Lista de Exercício 4 - Questão 4
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

class Letras:
    def qtd_consoantes():
        try:
            vogais = ["A","E","I","O","U"]

            consoantes = []

            for i in range(10):
                letra = input("Digite uma letra: ")

                if letra.upper() in vogais:
                    pass

                else:
                    consoantes.append(letra.upper())

            print(f"Número de consoantes: {len(consoantes)}")
            print(f"Consoantes: {', '.join(consoantes)}")
        
        except:
            print("Error")