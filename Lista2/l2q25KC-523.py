#Lista de Exercício 2 - Questão 25
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#25.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".



class InvestigacaoCrime:
    def fazer_perguntas(self):
        respostas = []
        perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]
        for pergunta in perguntas:
            while True:
                resposta = input(pergunta + " (Sim/Não): ").lower()
                if resposta in ["sim", "não"]:
                    break
                else:
                    print("Resposta inválida. Digite 'Sim' ou 'Não'.")
            respostas.append(resposta == "sim")
        return respostas
    def classificar_participacao(self, respostas):
        num_respostas_positivas = sum(respostas)
        if num_respostas_positivas == 2:
            classificacao = "Suspeita"
        elif 3 <= num_respostas_positivas <= 4:
            classificacao = "Cúmplice"
        elif num_respostas_positivas == 5:
            classificacao = "Assassino"
        else:
            classificacao = "Inocente"
        return classificacao
    def executar(self):
        respostas = self.fazer_perguntas()
        classificacao = self.classificar_participacao(respostas)
        print("Classificação:", classificacao)
investigacao = InvestigacaoCrime()
investigacao.executar()
