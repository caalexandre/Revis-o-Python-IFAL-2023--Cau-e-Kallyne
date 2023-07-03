#Lista de Exercício 8 - Questão 14
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
#  harry=funcionário("Harry",25000)
#  harry.aumentarSalario(10)

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def fichaFuncionario(self):
        return self.nome, self.salario

    def aumentarSalario(self, valor):
        self.salario += valor

try:
    func1 = Funcionario('Cauã', 700)

    print(f"Nome: {func1.fichaFuncionario()[0]}\n"
          f"Salário: {func1.fichaFuncionario()[1]}")

    func1.aumentarSalario(100)
    
    print(f"Nome: {func1.fichaFuncionario()[0]}\n"
          f"Salário: {func1.fichaFuncionario()[1]}")

except:
    print("Error")