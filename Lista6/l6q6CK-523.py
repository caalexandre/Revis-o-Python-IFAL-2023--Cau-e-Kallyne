#Lista de Exercício 6 - Questão 6
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
#
#Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

class DataNascimento:
    def __init__(self, data):
        self._data = data.split('/')

    def dataPorExtenso(self):
        mes = int(self._data[1])-1
        try:
            return f"Você nasceu em {self._data[0]} de {meses[mes]} de {self._data[2]}."

        except ValueError:
            return "Error"


d = input("Digite sua data de nascimento (dd/mm/aaa): ")

print(DataNascimento(d).dataPorExtenso())