#Lista de Exercício 2 - Questão 22
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#22.Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).



def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
def solicitar_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
    return numero
def main():
    numero = solicitar_numero()
    resultado = verificar_par_impar(numero)
    print("O número {} é {}".format(numero, resultado))
if __name__ == "__main__":
    main()
