#Lista de Exercício 8 - Questão 7
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#
#Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class Tamagushi:
    def __init__(self, nome, idade, fome, saude):
        self._nome = nome
        self._idade = idade
        self._fome = fome
        self._saude = saude
    
    def mudarNome(self, nomeNovo):
        if self.humor() == "Morto":
            print("Seu bixinho está morto, ação cancelada.")
    
        else:
            self._nome = nomeNovo
    
    def alimentar(self):
        if self.humor() == "Morto":
            print("Seu bixinho está morto, ação cancelada.")

        else: 
            if self._fome + 25 > 100:
                self._fome = 100
            else:
                self._fome += 25
        
    def cuidar(self):
        if self.humor() == "Morto":
            print("Seu bixinho está morto, ação cancelada.")
        
        else:
            if self._saude + 25 > 100:
                self._saude = 100
            else:
                self._saude += 25
    
    def humor(self):
        if ((self._saude+self._fome)/200) >= 75:
            return "Feliz"
    
        elif ((self._saude+self._fome)/200) >= 50:
            return "Impaciente"

        elif ((self._saude+self._fome)/200) >= 25:
            return "Irritado"

        elif ((self._saude+self._fome)/200) > 1:
            return "Fraco"

        if self._saude < 1 or self._fome < 1:
            return "Morto"

        else:
            return "Desconhecido"

    def status(self):
        return (f"Nome: {self._nome}\n"
                f"Idade: {self._idade}\n"
                f"Saúde: {self._saude}/100\n"
                f"Fome: {self._fome}/100\n"
                f"Status: {self.humor()}")


try:
    bicho1 = Tamagushi('Ti Bé', 69, 100, 100)
    print(bicho1.status())
    bicho1.alimentar()

except:
    print("Error")