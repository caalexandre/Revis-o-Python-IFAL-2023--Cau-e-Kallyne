#Lista de Exercício 8 - Questão 4
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Pessoa: Crie uma classe que modele uma pessoa:
#
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
    
    def envelhecer(self):
        self._idade += 1

        if self._nome.lower() == 'cauã':
            pass
        else:
            self._altura+= 0.5
    
    def engordar(self):
        self._peso += 5
    
    def emagrecer(self):
        self._peso -= 5

    def crescer(self):
        if self._nome.lower() == 'cauã':
            pass
        else:
            self._altura += 1

    def caracteristicas(self):
        return (f"Nome: {self._nome}\n"
                f"Idade: {self._idade}\n"
                f"Altura: {self._altura}\n"
                f"Peso: {self._peso}")


try:
    pessoa1 = Pessoa('Cauã', 18, 65, 162)
    print(pessoa1.caracteristicas())

    pessoa1.envelhecer()
    pessoa1.emagrecer()
    pessoa1.crescer()
    print(pessoa1.caracteristicas())

except:
    print("Error")
