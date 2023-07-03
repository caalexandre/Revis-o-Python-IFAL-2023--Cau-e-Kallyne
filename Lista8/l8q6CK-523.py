#Lista de Exercício 8 - Questão 6
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self, canal = 1, volume = 25):
        self._canal = canal
        self._volume = volume

    def mudarCanal(self, canalNovo):
        if canalNovo > 0 and canalNovo <= 15:
            self._canal = canalNovo

        else:
            print("Canal inválido.")
    
    def mudarVolume(self, valorNovo):
        if valorNovo >= 0 and valorNovo <= 100:
            self._volume = valorNovo
        
        else:
            print("Valor inválido.")
    
    def statusTV(self):
        return (f"Canal atual: {self._canal}\n"
                f"Volume atual: {self._volume}")

try:
    televisao = TV(2, 15)
    print(televisao.statusTV())

    televisao.mudarCanal(4)
    televisao.mudarVolume(50)
    print(televisao.statusTV())
except:
    print("Error")