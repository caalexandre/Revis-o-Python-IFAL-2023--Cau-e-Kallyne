#Lista de Exercício 3 - Questão 40
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

class Acidentes:
    def calcular_acidentes():
        try:
            total_cidade = 5

            maior_cidade = 0
            maior_indice = 0
            menor_cidade = 0
            menor_indice = float('inf')

            veiculos_total = 0

            qtd_menor_2000 = 0
            menor_2000 = 0

            for i in range(total_cidade):
                cidade = input("Digite o código da cidade: ")
                veiculos = int(input("Digite a quantidade de veículos (1999): "))
                acidentes = int(input("Digite a quanditade de acidentes (1999): "))
                
                veiculos_total += veiculos

                if acidentes > maior_indice:
                    maior_cidade = cidade
                    maior_indice = acidentes
                
                if acidentes < menor_indice:
                    menor_cidade = cidade
                    menor_indice = acidentes

                if veiculos < 2000:
                    menor_2000 += acidentes
                    qtd_menor_2000 += 1
                
            print(f"Maior indice de acidentes\n"
                  f"Cidade: {maior_cidade}\n"
                  f"Indice: {maior_indice}")
            
            print("="*30)

            print(f"Menor indice de acidentes\n"
                  f"Cidade: {menor_cidade}\n"
                  f"Indice: {menor_indice}")
            
            print("="*30)

            print(f"Média de carros de todas as cidades: {veiculos_total/5}")

            print("="*30)

            print(f"Média de acidentes nas cidades (menos de 2000 veiculos): {menor_2000/qtd_menor_2000:.2f}")

        except:
            print("Error")
        
Acidentes.calcular_acidentes()