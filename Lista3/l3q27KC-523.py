#Lista de Exercício 3 - Questão 27
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#27.Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.


class Turma:
    def __init__(self, numero_turma, quantidade_alunos):
        self.numero_turma = numero_turma
        self.quantidade_alunos = quantidade_alunos


class CalculadoraMediaTurmas:
    LIMITE_TURMAS = 10

    def __init__(self):
        self.turmas = []

    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def obter_quantidade_turmas(self):
        return len(self.turmas)

    def obter_quantidade_alunos_total(self):
        return sum(turma.quantidade_alunos for turma in self.turmas)

    def calcular_media_alunos_por_turma(self):
        quantidade_turmas = self.obter_quantidade_turmas()
        if quantidade_turmas == 0:
            return 0
        return self.obter_quantidade_alunos_total() / quantidade_turmas

    def adicionar_turmas_e_alunos(self):
        while len(self.turmas) < self.LIMITE_TURMAS:
            try:
                numero_turma = len(self.turmas) + 1
                quantidade_alunos = int(input(f"Digite a quantidade de alunos na turma {numero_turma}: "))
                if quantidade_alunos <= 0:
                    raise ValueError("A quantidade de alunos deve ser maior que zero.")
                if quantidade_alunos > 40:
                    raise ValueError("A quantidade de alunos não pode ser maior que 40.")
                turma = Turma(numero_turma, quantidade_alunos)
                self.adicionar_turma(turma)
            except ValueError as e:
                print(f"Erro: {e}")
            else:
                print("Turma adicionada com sucesso!")
                continuar = input("Deseja adicionar mais turmas? (S/N): ")
                if continuar.upper() != "S":
                    break

    def exibir_media_alunos_por_turma(self):
        media_alunos = self.calcular_media_alunos_por_turma()
        print(f"A média de alunos por turma é: {media_alunos:.2f}")


if __name__ == "__main__":
    calculadora = CalculadoraMediaTurmas()
    calculadora.adicionar_turmas_e_alunos()
    calculadora.exibir_media_alunos_por_turma()

