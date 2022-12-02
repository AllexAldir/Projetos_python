import pandas as pd

tabela_gerente = pd.read_excel("Gerentes.xlsx")


tabela_gerente.loc[:, "Vendas"] = 0
# print(tabela_gerente) 



# print(tabela_gerente.loc[tabela_gerente["ID Loja"] == "Shopping Barra",["Gerente","Vendas"]])
