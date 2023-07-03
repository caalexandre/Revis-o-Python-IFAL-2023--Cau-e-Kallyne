#Lista de Exercício 4 - Questão 23
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#alexandre       456123789
#anderson        1245698456
#antonio         123456456
#carlos          91257581
#cesar           987458
#rosemary        789456125
#Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
#ACME Inc.               Uso do espaço em disco pelos usuários
#------------------------------------------------------------------------
#Nr.  Usuário        Espaço utilizado     % do uso
#
#1    alexandre       434,99 MB             16,85%
#2    anderson       1187,99 MB             46,02%
#3    antonio         117,73 MB              4,56%
#4    carlos           87,03 MB              3,37%
#5    cesar             0,94 MB              0,04%
#6    rosemary        752,88 MB             29,16%
#
#Espaço total ocupado: 2581,57 MB
#Espaço médio ocupado: 430,26 MB
#O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

class Usuario:
    def __init__(self, nome, espaco):
        self.nome = nome
        self.espaco = espaco

def converter_bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def calcular_percentual(espaco, espaco_total):
    return (espaco / espaco_total) * 100

usuarios = []

with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        nome, espaco = linha.split()
        usuarios.append(Usuario(nome, int(espaco)))

espaco_total = sum(usuario.espaco for usuario in usuarios)
espaco_medio = espaco_total / len(usuarios)

usuarios.sort(key=lambda usuario: usuario.espaco, reverse=True)

with open("relatorio.txt", "w", encoding="utf-8") as relatorio:
    relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    relatorio.write("--------------------------------------------------------------\n")
    relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")

    for i, usuario in enumerate(usuarios, start=1):
        espaco_mb = converter_bytes_para_mb(usuario.espaco)
        percentual = calcular_percentual(usuario.espaco, espaco_total)
        relatorio.write(f"{i}    {usuario.nome.ljust(15)} {espaco_mb:.2f} MB {' ' * 16} {percentual:.2f}%\n")

    relatorio.write(f"\nEspaço total ocupado: {converter_bytes_para_mb(espaco_total):.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {converter_bytes_para_mb(espaco_medio):.2f} MB\n")

print("Relatório gerado com sucesso!")
