#Lista de Exercício 5 - Questão 6
#Dupla: 2020314273 - Cauã Alexandre e 2021327294 - Kallyne Ferro
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converter_horario(horas, minutos):
    if horas >= 0 and horas <= 11:
        periodo = 'A.M.'
        if horas == 0:
            horas = 12
    else:
        periodo = 'P.M.'
        if horas != 12:
            horas -= 12
    return horas, minutos, periodo

def exibir_horario(horas, minutos, periodo):
    print(f'{horas}:{minutos:02d} {periodo}')

while True:
    try:
        horas = int(input('Digite a hora (0-23): '))
        minutos = int(input('Digite os minutos (0-59): '))
        if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            raise ValueError
        horario_convertido = converter_horario(horas, minutos)
        exibir_horario(*horario_convertido)
        opcao = input('Deseja converter outro horário? (S/N): ')
        if opcao.upper() == 'N':
            break
        
    except ValueError:
        print('Entrada inválida. Digite novamente.')
