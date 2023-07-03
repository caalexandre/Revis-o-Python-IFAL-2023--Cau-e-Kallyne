#Lista de Exercício 5 - Questão 11
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

class Data:
    def __init__(self, data):
        self._data = data.split('/')

    def porExtenso(self):
        print
        mes = int(self._data[1])-1

        try:
            return f"{self._data[0]} de {meses[mes]} de {self._data[2]}"

        except ValueError:
            return "Error"

print(Data('20/12/2005').porExtenso())