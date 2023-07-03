#Lista de Exercício 7 - Questão 2
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

    def converter_bytes_para_megabytes(self):
        megabytes = self.espaco / (1024 * 1024)
        return round(megabytes, 2)

class Relatorio:
    def __init__(self, usuarios):
        self.usuarios = usuarios
        self.espaco_total = sum(usuario.espaco for usuario in usuarios)

    def calcular_percentual_espaco_utilizado(self, espaco_utilizado):
        percentual = (espaco_utilizado / self.espaco_total) * 100
        return round(percentual, 2)

    def gerar_relatorio(self):
        relatorio = []
        relatorio.append("ACME Inc.               Uso do espaço em disco pelos usuários")
        relatorio.append("-------------------------------------------------------------")
        relatorio.append("Nr.  Usuário        Espaço utilizado     % do uso")
        for i, usuario in enumerate(self.usuarios, start=1):
            espaco_mb = usuario.converter_bytes_para_megabytes()
            percentual = self.calcular_percentual_espaco_utilizado(usuario.espaco)
            linha_relatorio = f"{i:<5} {usuario.nome:<15} {espaco_mb:>15.2f} MB {percentual:>10.2f}%"
            relatorio.append(linha_relatorio)

        relatorio.append("")
        relatorio.append(f"Espaço total ocupado: {Usuario('', self.espaco_total).converter_bytes_para_megabytes():.2f} MB")
        relatorio.append(f"Espaço médio ocupado: {Usuario('', self.espaco_total / len(self.usuarios)).converter_bytes_para_megabytes():.2f} MB")

        return relatorio

    def escrever_relatorio_arquivo(self):
        with open('relatorio.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('\n'.join(self.gerar_relatorio()))

def ler_usuarios_arquivo():
    usuarios = []
    with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            nome, espaco = linha.strip().split()
            usuarios.append(Usuario(nome, int(espaco)))
    return usuarios


usuarios = ler_usuarios_arquivo()
relatorio = Relatorio(usuarios)
relatorio.escrever_relatorio_arquivo()
