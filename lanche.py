# import matplotlib as plt
import time

print("""
Cardápio:
0 - Suco                R$:3.00
1 - Pizza               R$:5.00
2 - Hamburgue           R$:7.00
3 - Coxinha             R$:4.00
4 - Refrigerante        R$:5.00        
""")

l_comidas = ["Suco", "Pizza", "Hamburgue", "Coxinha", "Refrigerante"]
preco = [3,5,7,4,5]
soma = 0
repetir = "sim"
c = 0  

while repetir == "sim":
    produto = input("Digite o nome do produto o qual você deseja: ").capitalize()

    while produto not in l_comidas:
        produto = input("Nome não identificado na lista.. Tente novamente: ").capitalize()

    print(f"produto escolhido: {produto}")

    indice = l_comidas.index(produto)
    preco_ = preco[indice]
    soma += preco_
    
    repetir = input("Deseja repetir o a compra? 'sim' ou 'não': ").lower()
    time.sleep(2)

print(f"Total da fatura é de: {soma} R$")