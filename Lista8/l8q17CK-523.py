#Lista de Exercício 8 - Questão 17
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

import random

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

def criar_fazenda(num_bichinhos):
    fazenda = []
    for i in range(num_bichinhos):
        nome = f"Bichinho {i+1}"
        idade = random.randint(1, 10)
        fome = random.randint(1, 100)
        saude = random.randint(1, 100)
        bichinho = Tamagushi(nome, idade, fome, saude)
        fazenda.append(bichinho)
    return fazenda

def mostrar_status_fazenda(fazenda):
    for bichinho in fazenda:
        print(bichinho.status())
        print()

def alimentar_todos(fazenda, quantidade):
    for bichinho in fazenda:
        bichinho.alimentar(quantidade)

def brincar_todos(fazenda, tempo):
    for bichinho in fazenda:
        bichinho.brincar(tempo)

def cuidar_todos(fazenda):
    for bichinho in fazenda:
        bichinho.cuidar()

def opcoes_menu():
    print("-------- Fazenda de Bichinhos --------")
    print("1. Mostrar status de todos os bichinhos")
    print("2. Alimentar todos os bichinhos")
    print("3. Brincar com todos os bichinhos")
    print("4. Cuidar de todos os bichinhos")
    print("5. Sair")
    print("--------------------------------------")

num_bichinhos = 3
fazenda = criar_fazenda(num_bichinhos)

while True:
    opcoes_menu()
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        mostrar_status_fazenda(fazenda)

    elif opcao == 2:
        quantidade = int(input("Digite a quantidade de comida a fornecer: "))
        alimentar_todos(fazenda, quantidade)

    elif opcao == 3:
        tempo = int(input("Digite o tempo de brincadeira: "))
        brincar_todos(fazenda, tempo)

    elif opcao == 4:
        cuidar_todos(fazenda)

    elif opcao == 5:
        break

    else:
        print("Opção inválida. Digite novamente.")

