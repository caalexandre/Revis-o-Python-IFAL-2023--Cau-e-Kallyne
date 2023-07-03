#Lista de Exercício 3 - Questão 25
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#25.Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.


def calcular_media(idades):
    quantidade = len(idades)
    soma = sum(idades)
    media = soma / quantidade
    return media


def classificar_turma(media_idades):
    if 0 <= media_idades <= 25:
        return "Turma Jovem"
    elif 26 <= media_idades <= 60:
        return "Turma Adulta"
    else:
        return "Turma Idosa"


def ler_idade(numero):
    idades = []
    for i in range(numero):
        while True:
            try:
                idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
                if idade < 0:
                    raise ValueError("Digite uma idade válida.")
                idades.append(idade)
                break
            except ValueError:
                print("Valor inválido. Digite uma idade válida.")
    return idades


numero_pessoas = 0
while True:
    try:
        numero_pessoas = int(input("Digite o número de pessoas: "))
        if numero_pessoas < 1:
            raise ValueError("Digite um número de pessoas válido.")
        break
    except ValueError:
        print("Valor inválido. Digite um número de pessoas válido.")

idades = ler_idade(numero_pessoas)

media_idades = calcular_media(idades)

classificacao = classificar_turma(media_idades)

print(f"A média de idade da turma é: {media_idades}")
print(f"Classificação da turma: {classificacao}")
