# 12) Construir um programa que leia um valor numérico inteiro e apresente como
#     resultado os seus valores: sucessor e antecessor.
def valid_num(num):
    return num + 1, num - 1

num = int(input("Digite um número: "))
print(f"número que sucessede e número que antecessede : {valid_num(num)}")
