#Lista de Exercício 1 - Questão 18
#Dupla: 2020314273 - Cauã Alexandre Torres de Holanda e 2021327294 - Kallyne Ferro Veiga 
#Disciplina: Programação Web
#Professor: Ítalo Arruda

#18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math

def solicitar_dados():
    while True:
        try:
            tamanho_arquivo_mb = float(input("Informe o tamanho do arquivo para download (em MB): "))
            velocidade_internet_mbps = float(input("Informe a velocidade do link de Internet (em Mbps): "))
            return tamanho_arquivo_mb, velocidade_internet_mbps
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
   
    velocidade_internet_mbps = velocidade_internet_mbps / 8

 
    tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mbps

    tempo_download_minutos = math.ceil(tempo_download_segundos / 60)

    return tempo_download_minutos

def exibir_resultado(tempo_download_minutos):
    print("O tempo aproximado de download é de", tempo_download_minutos, "minutos.")

def main():
    tamanho_arquivo_mb, velocidade_internet_mbps = solicitar_dados()
    tempo_download_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)
    exibir_resultado(tempo_download_minutos)

main()
