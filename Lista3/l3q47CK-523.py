#Lista de Exercício 3 - Questão 47
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Aparecido Parente
#Nota: 9.9
#Nota: 7.5
#Nota: 9.5
#Nota: 8.5
#Nota: 9.0
#Nota: 8.5
#Nota: 9.7
#
#Resultado final:
#Atleta: Aparecido Parente
#Melhor nota: 9.9
#Pior nota: 7.5
#Média: 9,04

class Notas:
    def __init__(self, nome):
        self._nome = nome
    
    def calcular_nota(self):
        try:
            notas = []


            melhor_nota = 0
            pior_nota = float('inf')

            total = 0

            for i in range(1,11):
                nota = float(input("Digite o valor da nota: "))

                total += nota
                notas.append(nota)

                if nota > melhor_nota:
                    melhor_nota = nota
                
                if nota < pior_nota:
                    pior_nota = nota

            print(f"Atleta: {self._nome}")
            for i in notas:
                print(f"Nota: {i}")

            print("\nResultado final:\n"
                f"Atleta: {self._nome}\n"
                f"Melhor nota: {melhor_nota}\n"
                f"Pior nota: {pior_nota}\n"
                f"Média: {total/5}")
            
        except:
            print("Error")


x = input("Digite o nome do atleta: ")

atleta1 = Notas(x)

atleta1.calcular_nota()