#Lista de Exercício 2 - Questão 18
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#18.Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


class DataValida:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0
    def ler_data(self):
        while True:
            try:
                data = input("Digite uma data no formato dd/mm/aaaa: ")
                partes = data.split("/")
                if len(partes) != 3:
                    raise ValueError
                self.dia = int(partes[0])
                self.mes = int(partes[1])
                self.ano = int(partes[2])
                break
            except ValueError:
                print("Data inválida. Digite a data no formato dd/mm/aaaa.")
    def verificar_data(self):
        meses_com_31_dias = [1, 3, 5, 7, 8, 10, 12]

        if self.mes < 1 or self.mes > 12:
            return False

        if self.mes in meses_com_31_dias and (self.dia < 1 or self.dia > 31):
            return False

        if self.mes == 2:
            if (self.ano % 4 == 0 and self.ano % 100 != 0) or self.ano % 400 == 0:
                if self.dia < 1 or self.dia > 29:
                    return False
            else:
                if self.dia < 1 or self.dia > 28:
                    return False

        if self.dia < 1 or self.dia > 30:
            return False

        return True
    def exibir_resultado(self, data_valida):
        if data_valida:
            print("A data {} é válida.".format(self.formatar_data()))
        else:
            print("A data {} é inválida.".format(self.formatar_data()))
    def formatar_data(self):
        return "{:02d}/{:02d}/{:04d}".format(self.dia, self.mes, self.ano)
    def verificar_data_valida(self):
        self.ler_data()
        data_valida = self.verificar_data()
        self.exibir_resultado(data_valida)
def main():
    data = DataValida()
    data.verificar_data_valida()
if __name__ == "__main__":
    main()
