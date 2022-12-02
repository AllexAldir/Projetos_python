# 10) Elaborar um programa que leia dois valores numéricos reais desconhecidos
#     representados pelas variáveis A e B. Calcular e apresentar os resultados das quatro
#     operações aritméticas básicas(soma, subtração, divisão e multiplicação).

def cal(a, b):
    return a+b, a*b, a-b, a/b
a = int(input("Digite um primeiro número: "))
b = int(input("Digite segundo número: "))

print(f"a soma de a+b, axb, a-b, a/b = {cal(a,b)}")

