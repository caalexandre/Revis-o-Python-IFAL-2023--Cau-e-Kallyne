#Lista de Exercício 3 - Questão 3
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#3.Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


def ler_informacoes():
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) <= 3:
            print("Erro: O nome deve ter mais de 3 caracteres.")
        else:
            break
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0 or idade > 150:
                print("Erro: A idade deve estar entre 0 e 150.")
            else:
                break
        except ValueError:
            print("Erro: Digite um valor numérico para a idade.")
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario <= 0:
                print("Erro: O salário deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("Erro: Digite um valor numérico para o salário.")
    while True:
        sexo = input("Digite seu sexo (f/m): ")
        if sexo.lower() not in ['f', 'm']:
            print("Erro: Digite 'f' para feminino ou 'm' para masculino.")
        else:
            break
    while True:
        estado_civil = input("Digite seu estado civil (s/c/v/d): ")
        if estado_civil.lower() not in ['s', 'c', 'v', 'd']:
            print("Erro: Digite 's' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado.")
        else:
            break
    return nome, idade, salario, sexo, estado_civil
nome, idade, salario, sexo, estado_civil = ler_informacoes()
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
