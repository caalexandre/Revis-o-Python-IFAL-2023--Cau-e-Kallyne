#Lista de Exercício 3 - Questão 2
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


def verificar_senha():
    while True:
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
        if password == username:
            print("Erro: A senha não pode ser igual ao nome de usuário.")
        else:
            return username, password
username, password = verificar_senha()
print("Nome de usuário:", username)
print("Senha:", password)
