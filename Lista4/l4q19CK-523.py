#Lista de Exercício 4 - Questão 19
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
#"Qual o melhor Sistema Operacional para uso em servidores?"
#
#As possíveis respostas são:
#
#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro
#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
#Sistema Operacional     Votos   %
#-------------------     -----   ---
#Windows Server           1500   17%
#Unix                     3500   40%
#Linux                    3000   34%
#Netware                   500    5%
#Mac OS                    150    2%
#Outro                     150    2%
#-------------------     -----
#Total                    8800
#
#O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

class Enquete:
    def __init__(self):
        self.opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
        self.votos = [0] * 7

    def computar_voto(self, opcao):
        if opcao < 0 or opcao > 6:
            raise ValueError("Opção inválida.")
        self.votos[opcao] += 1

    def calcular_percentual(self, votos_opcao, total_votos):
        return (votos_opcao / total_votos) * 100

    def exibir_resultado(self):
        total_votos = sum(self.votos)
        print("Sistema Operacional\tVotos\t%")
        print("-------------------\t-----\t---")

        for i, opcao in enumerate(self.opcoes):
            votos = self.votos[i]
            percentual = self.calcular_percentual(votos, total_votos)
            print(f"{opcao:20s}\t{votos:5d}\t{percentual:.1f}%")

        print("-------------------\t-----\t---")
        print(f"Total\t\t\t{total_votos}\n")

        index_vencedor = self.votos.index(max(self.votos))
        votos_vencedor = self.votos[index_vencedor]
        percentual_vencedor = self.calcular_percentual(votos_vencedor, total_votos)
        vencedor = self.opcoes[index_vencedor]

        print(f"O Sistema Operacional mais votado foi o {vencedor}, com {votos_vencedor} votos, correspondendo a {percentual_vencedor:.1f}% dos votos.")


enquete = Enquete()

print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?\n")
print("Opções:")
for i, opcao in enumerate(enquete.opcoes):
    print(f"{i+1}-{opcao}")

while True:
    try:
        opcao_voto = int(input("Digite o número da opção desejada (0 para encerrar): "))
        if opcao_voto == 0:
            break
        enquete.computar_voto(opcao_voto - 1)
    except ValueError:
        print("Valor inválido. Digite um número válido de 0 a 6.")

enquete.exibir_resultado()
