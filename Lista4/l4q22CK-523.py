#Lista de Exercício 4 - Questão 22
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#Quantidade de mouses: 100
#
#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%

class Mouse:
    def __init__(self, identificacao, defeito):
        self.identificacao = identificacao
        self.defeito = defeito

mouses = []
tipos_defeito = {
    1: "necessita da esfera",
    2: "necessita de limpeza",
    3: "necessita troca do cabo ou conector",
    4: "quebrado ou inutilizado"
}

while True:
    identificacao = int(input("Digite o número de identificação do mouse (0 para encerrar): "))
    if identificacao == 0:
        break

    defeito = int(input("Digite o tipo de defeito do mouse (1-4): "))
    if defeito < 1 or defeito > 4:
        print("Defeito inválido. Digite um valor entre 1 e 4.")
        continue

    mouses.append(Mouse(identificacao, defeito))

quantidade_mouses = len(mouses)

print("\nRelatório de Levantamento de Mouses")
print("===================================\n")
print(f"Quantidade de mouses: {quantidade_mouses}\n")
print("Situação                        Quantidade              Percentual")

for defeito in range(1, 5):
    quantidade_defeito = sum(1 for mouse in mouses if mouse.defeito == defeito)
    percentual = (quantidade_defeito / quantidade_mouses) * 100
    print(f"{defeito}- {tipos_defeito[defeito].ljust(30)} {quantidade_defeito} {percentual:.0f}%")

