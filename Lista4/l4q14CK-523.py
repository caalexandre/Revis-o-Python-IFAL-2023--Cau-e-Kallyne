#Lista de Exercício 4 - Questão 14
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

class Assassinato:
    def interrogatorio():
        try:
            perguntas = ["Telefonou para a vitima?", "Esteve no local do crime?", "Mora perto da vitima?", "Devia para a vitima?", "Já trabalhou com a vitima?"]
            total = 0

            print("Responda com s/n...")

            for pergunta in perguntas:
                p = input(f"{pergunta} ")

                if p.lower() == 's':
                    total += 1

            if total == 2:
                print("Suspeita")

            elif total == 3 or total == 4:
                print("Cúmplice")

            elif total >= 5:
                print("Assassino")

            else:
                print("Inocente")
        
        except:
            print("Error")

Assassinato.interrogatorio()