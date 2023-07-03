#Lista de Exercício 3 - Questão 26
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#26.Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


class Eleicao:
    def __init__(self, num_candidatos):
        self.num_candidatos = num_candidatos
        self.votos = [0] * self.num_candidatos

    def votar(self, candidato):
        if 1 <= candidato <= self.num_candidatos:
            self.votos[candidato - 1] += 1
            print("Voto registrado com sucesso!")
        else:
            print("Candidato inválido!")

    def exibir_resultados(self):
        print("Resultado da eleição:")
        for i in range(self.num_candidatos):
            print(f"Candidato {i+1}: {self.votos[i]} voto(s)")


def main():
    try:
        num_eleitores = int(input("Digite o número total de eleitores: "))
        eleicao = Eleicao(3)  # Supondo que existam 3 candidatos

        for _ in range(num_eleitores):
            voto = int(input("Digite o número do candidato que deseja votar: "))
            eleicao.votar(voto)

        eleicao.exibir_resultados()

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro.")

if __name__ == "__main__":
    main()
