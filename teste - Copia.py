import pandas as pd


vendas_semanais = {"produtos":["Mouse","Gabinte","Teclado"],"Quantidade":[2,1,5],"valor":[15,300,45],}

tb_vendas = pd.DataFrame(vendas_semanais)
print(tb_vendas)


