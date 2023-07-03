#Lista de Exercício 3 - Questão 5
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#5.Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


def calcular_populacao_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
    anos = 0
    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_crescimento_a
        populacao_b += populacao_b * taxa_crescimento_b
        anos += 1
    return anos


while True:
    try:
        populacao_a = int(input("Informe a população do país A: "))
        taxa_crescimento_a = float(input("Informe a taxa de crescimento do país A (em decimal): "))
        populacao_b = int(input("Informe a população do país B: "))
        taxa_crescimento_b = float(input("Informe a taxa de crescimento do país B (em decimal): "))
        
        if populacao_a <= 0 or taxa_crescimento_a <= 0 or populacao_b <= 0 or taxa_crescimento_b <= 0:
            raise ValueError("Os valores informados devem ser maiores que zero.")
        
        anos_necessarios = calcular_populacao_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)
        
        print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")
        
        repetir = input("Deseja realizar outra operação? (s/n): ")
        if repetir.lower() != "s":
            break
        
    except ValueError as e:
        print(f"Erro: {e}")

