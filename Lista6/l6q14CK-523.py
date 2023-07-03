#Lista de Exercício 6 - Questão 14
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

class LeetSpeakGenerator:
    def __init__(self):
        self.leet_dict = {
            'A': '4',
            'E': '3',
            'G': '6',
            'I': '1',
            'O': '0',
            'S': '5',
            'T': '7'
        }

    def gerar_leet_speak(self, texto):
        try:
            texto_leet = ""
            for letra in texto:
                letra_upper = letra.upper()
                if letra_upper in self.leet_dict:
                    letra_leet = self.leet_dict[letra_upper]
                    texto_leet += letra_leet
                else:
                    texto_leet += letra

            return texto_leet
    
        except:
            print("Error")

texto_original = input("Digite um texto para ser convertido para Leet Speak: ")

leet_generator = LeetSpeakGenerator()

texto_leet = leet_generator.gerar_leet_speak(texto_original)

print("Texto em Leet Speak: ", texto_leet)
