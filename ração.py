# 4) Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os
# quais fornece a quantidade de ração em gramas. A quantidade diária de ração
# fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do
# saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre
# quanto restará de ração no saco após cinco dias.

pse_ra = float(input("Digite aqui o peso do saco de ração (kg): "))
pse_grama = pse_ra*1000
gato = pse_grama/2

for i in range(0,5):
    pse_grama = pse_grama/2
print(f"Quanto ficou em gramas no saco de ração: {pse_grama}")
    


