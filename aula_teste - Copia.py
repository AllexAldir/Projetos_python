import pandas as pd
# Tabela exemplo

dic_ = {"Camisas Masculinas": ["Jurassic World","Wolwerine","Lebron James"],"Quantidade":[2,2,2]}

tabela_vendas = pd.DataFrame(dic_)

tabela_vendas["Vendas"] = tabela_vendas["Quantidade"] * (50,34,78) #Os itens vão passando de 1 em 1(multiplicando)

valores_codn = tabela_vendas.loc[tabela_vendas["Camisas Masculinas"] == "Jurassic World",["Camisas Masculinas","Quantidade","Vendas"]]

print(tabela_vendas.describe()) 
