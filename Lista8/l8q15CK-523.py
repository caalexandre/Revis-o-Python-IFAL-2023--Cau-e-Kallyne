#Lista de Exercício 8 - Questão 15
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.


class Tamagushi:
    def __init__(self, nome, idade, fome, saude):
        self._nome = nome
        self._idade = idade
        self._fome = fome
        self._saude = saude
    
    def mudarNome(self, nomeNovo):
        if self.humor() == "Morto":
            print("Seu bichinho está morto, ação cancelada.")
        else:
            self._nome = nomeNovo
    
    def alimentar(self, quantidade):
        if self.humor() == "Morto":
            print("Seu bichinho está morto, ação cancelada.")
        else: 
            if self._fome + quantidade > 100:
                self._fome = 100
            else:
                self._fome += quantidade
    
    def brincar(self, tempo):
        if self.humor() == "Morto":
            print("Seu bichinho está morto, ação cancelada.")
        else:
            if self._fome - tempo > 0:
                self._fome -= tempo
            else:
                self._fome = 0
    
    def cuidar(self):
        if self.humor() == "Morto":
            print("Seu bichinho está morto, ação cancelada.")
        else:
            if self._saude + 25 > 100:
                self._saude = 100
            else:
                self._saude += 25
    
    def humor(self):
        if ((self._saude + self._fome) / 200) >= 75:
            return "Feliz"
        elif ((self._saude + self._fome) / 200) >= 50:
            return "Impaciente"
        elif ((self._saude + self._fome) / 200) >= 25:
            return "Irritado"
        elif ((self._saude + self._fome) / 200) > 1:
            return "Fraco"
        elif self._saude < 1 or self._fome < 1:
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
    bicho1.alimentar(30)
    bicho1.brincar(20)
    print(bicho1.status())

except:
    print("Error")
