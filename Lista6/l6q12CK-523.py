#Lista de Exercício 6 - Questão 12
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
#
#Valida e corrige número de telefone
#Telefone: 461-0133
#Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 3461-0133

class ValidadorTelefone:
    def __init__(self, telefone):
        self.telefone = telefone

    def validar(self):
        try:
            telefone_formatado = self.telefone.replace("-", "")
            telefone_formatado = telefone_formatado.replace(" ", "")
            telefone_formatado = telefone_formatado.replace(".", "")
            telefone_formatado = telefone_formatado.replace("(", "")
            telefone_formatado = telefone_formatado.replace(")", "")

            if len(telefone_formatado) == 7:
                telefone_corrigido = "3" + telefone_formatado
                telefone_corrigido_formatado = telefone_corrigido[:4] + "-" + telefone_corrigido[4:]
                return telefone_corrigido, telefone_corrigido_formatado
            elif len(telefone_formatado) == 8:
                telefone_corrigido_formatado = telefone_formatado[:4] + "-" + telefone_formatado[4:]
                return telefone_formatado, telefone_corrigido_formatado
            else:
                raise ValueError("Número de telefone inválido. Verifique se possui 7 ou 8 dígitos.")
        except:
            raise ValueError("Número de telefone inválido. Verifique o formato.")

telefone = input("Digite o número de telefone: ")

validador = ValidadorTelefone(telefone)
try:
    telefone_corrigido, telefone_corrigido_formatado = validador.validar()
    print("Telefone corrigido sem formatação:", telefone_corrigido)
    print("Telefone corrigido com formatação:", telefone_corrigido_formatado)
except ValueError as e:
    print("Erro:", str(e))