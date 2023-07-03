#Lista de Exercício 3 - Questão 44
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos 
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

class Eleicao:
    def votacao():
        try:
            candidato1 = 0
            candidato2 = 0
            candidato3 = 0
            candidato4 = 0
            nulo = 0
            branco = 0

            print("Candidatos | Códigos\n"
                "Cauã               1\n"
                "Niedson            2\n"
                "Bruno              3\n"
                "Ugu                4\n"
                "Voto Nulo          5\n"
                "Voto em Branco     6\n")


            while(True):
                voto = int(input("Digite o código do candidato: "))

                if voto == 1:
                    candidato1 += 1
                
                elif voto == 2:
                    candidato2 += 1
                
                elif voto == 3:
                    candidato3 += 1

                elif voto == 4:
                    candidato4 += 1

                elif voto == 5:
                    nulo += 1
                
                elif voto == 6:
                    branco += 1
                
                elif voto == 0:
                    break

                else:
                    print("Valor inválido")

            total = (candidato1+candidato2+candidato3+candidato4+branco+nulo)
        

            print("="*10+"RESULTADO"+"="*10)
            print(f"Cauã:                 {candidato1} votos\n"
                  f"Niedson:              {candidato2} votos\n"
                  f"Bruno:                {candidato3} votos\n"
                  f"Ugu:                  {candidato4} votos\n"
                  f"Voto Nulo:            {nulo} votos\n"
                  f"Voto em Branco        {branco} votos")
            print("="*9+"PORCENTAGEM"+"="*9)
            print(f"Voto Nulo:             {(nulo*100)/total:.2f}%\n"
                  f"Voto em Branco:        {(branco*100)/total:.2f}%")
            print("="*29)

        except:
            print("Error")

Eleicao.votacao()
