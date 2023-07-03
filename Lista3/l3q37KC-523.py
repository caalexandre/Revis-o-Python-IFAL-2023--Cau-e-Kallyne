#Lista de Exercício 3 - Questão 37
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda


#37.Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes



class Cliente:
    def __init__(self, codigo, altura, peso):
        self.codigo = codigo
        self.altura = altura
        self.peso = peso


def realizar_senso():
    clientes = []

    while True:
        codigo = input("Digite o código do cliente (ou 0 para encerrar): ")

        if codigo == '0':
            break

        try:
            altura = float(input("Digite a altura do cliente (em metros): "))
            peso = float(input("Digite o peso do cliente (em kg): "))

            cliente = Cliente(codigo, altura, peso)
            clientes.append(cliente)

        except ValueError:
            print("Valor inválido. Digite novamente.")

    if len(clientes) == 0:
        print("Nenhum cliente foi registrado.")
        return

    cliente_mais_alto = max(clientes, key=lambda c: c.altura)
    cliente_mais_baixo = min(clientes, key=lambda c: c.altura)
    cliente_mais_gordo = max(clientes, key=lambda c: c.peso)
    cliente_mais_magro = min(clientes, key=lambda c: c.peso)

    media_alturas = sum(c.altura for c in clientes) / len(clientes)
    media_pesos = sum(c.peso for c in clientes) / len(clientes)

    print("\nResultados do senso:")
    print(f"Mais alto: Código {cliente_mais_alto.codigo}, Altura {cliente_mais_alto.altura:.2f}m, Peso {cliente_mais_alto.peso:.2f}kg")
    print(f"Mais baixo: Código {cliente_mais_baixo.codigo}, Altura {cliente_mais_baixo.altura:.2f}m, Peso {cliente_mais_baixo.peso:.2f}kg")
    print(f"Mais gordo: Código {cliente_mais_gordo.codigo}, Altura {cliente_mais_gordo.altura:.2f}m, Peso {cliente_mais_gordo.peso:.2f}kg")
    print(f"Mais magro: Código {cliente_mais_magro.codigo}, Altura {cliente_mais_magro.altura:.2f}m, Peso {cliente_mais_magro.peso:.2f}kg")
    print(f"Média das alturas: {media_alturas:.2f}m")
    print(f"Média dos pesos: {media_pesos:.2f}kg")
realizar_senso()
