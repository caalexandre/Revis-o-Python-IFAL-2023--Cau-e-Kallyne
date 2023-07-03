#Lista de Exercício 7 - Questão 1
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
#O arquivo de entrada possui o seguinte formato:
#200.135.80.9
#192.168.1.1
#8.35.67.74
#257.32.4.5
#85.345.1.2
#1.2.3.4
#9.8.234.5
#192.168.0.256
#O arquivo de saída possui o seguinte formato:
#[Endereços válidos:]
#200.135.80.9
#192.168.1.1
#8.35.67.74
#1.2.3.4
#
#[Endereços inválidos:]
#257.32.4.5
#85.345.1.2
#9.8.234.5
#192.168.0.256

class IPValidator:
    @staticmethod
    def validar_endereco_ip(ip):
        numeros = ip.split('.')
        if len(numeros) != 4:
            return False
        for numero in numeros:
            if not numero.isdigit() or int(numero) < 0 or int(numero) > 255:
                return False
        return True


def gerar_relatorio_enderecos(input_file, output_file):
    enderecos_validos = []
    enderecos_invalidos = []

    with open(input_file, 'r') as file:
        for line in file:
            ip = line.strip()
            if IPValidator.validar_endereco_ip(ip):
                enderecos_validos.append(ip)
            else:
                enderecos_invalidos.append(ip)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("[Endereços válidos:]\n")
        for endereco in enderecos_validos:
            file.write(endereco + "\n")

        file.write("\n[Endereços inválidos:]\n")
        for endereco in enderecos_invalidos:
            file.write(endereco + "\n")


input_file = 'enderecos_ip.txt'
output_file = 'relatorio_enderecos.txt'

gerar_relatorio_enderecos(input_file, output_file)