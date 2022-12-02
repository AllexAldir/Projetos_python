# trabalhando com pandas
import pandas as pd
import numpy as nb
import openpyxl as opn
# tabela = pd.DataFrame cria uma tabela normal 


#Método mais comum utilizando um dicionário


# vendas = {"data":["15/02/2021","16/02/2021"], "valor":[500,30], "produto":["feijão","Arroz"], "qtde": [50,70],}

# tabela_vendas = pd.DataFrame(vendas) #Cria tabela de acordo como meu dicionário

# print(tabela_vendas)


tabela_excel = pd.read_excel("Vendas.xlsx")
tabela_gerentes = pd.read_excel("Gerentes.xlsx")
# print(tabela_excel)
# print(tabela_excel.head(100)) #Mostra os 5 primeiros itens da minha tabela... se quiser colocar mais 
                                #basta acrescentar no parâmentro a quantidade...

# print(tabela_excel.shape) #Aqui irá mostrar a tabela e sua quantidade de colunas e linhas...
                            #Método bom para mostrar quantas linha e colunas tem na tabela mais rápido

# print(tabela_excel.describe()) #Aqui mostra o resumo do faturamento de acordo com a tabela:


#Editando tabela:

# produto = tabela_excel[["Produto","ID Loja"]]   #Mostrará somente os itens "produto" da minha tabela
# print(produto)

#Pegando uma linha da tabela:

# print(tabela_excel.loc[1:5])          #Pegará um item de acordo com esse indice


# pegando item com uma condição

# print(tabela_excel.loc[tabela_excel["ID Loja"] == "Norte Shopping"])

#pegando várias linhas e colunas usando loc

# linhas_colun = tabela_excel.loc[tabela_excel["ID Loja"] == "Norte Shopping", ["ID Loja","Produto","Quantidade"]]
# print(linhas_colun)

# pegando um item especifico com o "loc"

# print(tabela_excel.loc[1, "Produto"]) 


# adicionando uma coluna a partir de uma coluna que já existe

# tabela_excel["Comissão"] = tabela_excel["Valor Final"] * 0.05           #Aqui pega o valor da minha tabela e faço uma ação
#                                                                         #no caso está pegando os valores da coluna "                                                                          "valor final" e multiplicando por 5%
# print(tabela_excel)


#Criando uma coluna com o valor padrão:

tabela_excel.loc[:,"Imposto"] = 0                   #Atribuindo o nome da minha nova coluna com o valor "0"

# print(tabela_excel)

tabela_excel = tabela_excel.append(tabela_gerentes) #Adicionando outra tabela... tabela + tabela

# print(tabela_excel)

# tabela_excel = tabela_excel.drop(0, axis = 0 ) #Excluindo linha , axis= eixo 
# print(tabela_excel)

# tabela_excel = tabela_excel.dropna()
# print(tabela_excel)


tabela_excel["Imposto"] = tabela_excel["Imposto"].fillna(tabela_excel["Imposto"].mean())
# print(tabela_excel)                             #Metodo comum preencher com a méida da coluna

transacoes = tabela_excel["ID Loja"].value_counts()
# print(transacoes)                                   #Mostra a quantidade de transações de acordo com uma coluna


faturamento = tabela_excel[["Produto", "Valor Final"]].groupby("Produto").sum()
print(faturamento)                              #Mostra um agrupamento mostrando com alguns parâmetros com: 
                                                #Soma,Média(mean)

#Passando uma informação de uma tabela para outra:

# ex:
#gerentes_df = pd.read_execel("Gerentes")
# tabela  = tabela.merge(Gerentes)
# print(tabela)