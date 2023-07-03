#Lista de Exercício 6 - Questão 9
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

class Documentacao:
    def __init__(self, cpf):
        self._cpf = cpf.replace('-','.').split('.')
    
    def validarCPF(self):
        if len(self._cpf) != 11:
            return False

        if self._cpf == self._cpf[0] * 11:
            return False

        soma = 0
        for i in range(9):
            soma += int(self._cpf[i]) * (10 - i)
        digito_verificador1 = (soma * 10) % 11
        if digito_verificador1 == 10:
            digito_verificador1 = 0

        soma = 0
        for i in range(10):
            soma += int(self._cpf[i]) * (11 - i)
        digito_verificador2 = (soma * 10) % 11
        if digito_verificador2 == 10:
            digito_verificador2 = 0

        if int(self._cpf[9]) == digito_verificador1 and int(self._cpf[10]) == digito_verificador2:
            return True
        else:
            return False

try:
    d = input("Digite seu CPF (xxx.xxx.xxx-xx): ")

    if (Documentacao(d).validarCPF()) == False:
        print("CPF inválido")

    else:
        print("CPF validado!")

except:
    print("Error")