#Lista de Exercício 8 - Questão 13
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def ficha(self):
        return self.nome, self.salario

try:
    func1 = Funcionario('Cauã', 700)

    print(f"Nome: {func1.ficha()[0]}\n"
        f"Salário: {func1.ficha()[1]}")

except:
    print("Error")
        