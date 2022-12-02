import pandas as pd
# import numpy as np
# from colorama import Fore
# import matplotlib.pyplot as plt

tabela = pd.DataFrame()
mes = []
valor = []

for i in range(0,1):
    mes.append(input("Digite o mês da venda: "))
    print(mes)
    valor.append(float(input("Digite o valor da venda: ")))
    print(valor)
    # tabela[f"{mes}"] = valor                          #tentativa de criar a tebela sem sucesso

tabela["meses"] = mes
tabela["valores"] = valor






