#Lista de Exercício 8 - Questão 16
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.

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
    
    def __str__(self):
        return (f"Nome: {self._nome}\n"
                f"Idade: {self._idade}\n"
                f"Saúde: {self._saude}\n"
                f"Fome: {self._fome}")

try:
    bicho1 = Tamagushi('Ti Bé', 69, 100, 100)
    print(bicho1.status())
    bicho1.alimentar(30)
    bicho1.brincar(20)
    print(bicho1.status())
    
    opcao_secreta = 999
    if opcao_secreta == 999:
        print(bicho1)

except:
    print("Error")