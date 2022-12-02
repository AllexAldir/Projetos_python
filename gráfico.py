import matplotlib.pyplot as plt
import numpy as np

passar = 6
notas = []
notas_n = []
repetir = 'sim'

while repetir == 'sim':

    notas_ = float(input("Digite aqui a nota do aluno: "))

    if notas_ > passar:
        notas.append(notas_)
    else:                       #estrutura para saber se a nota será maior que "6" ou não
        notas_n.append(notas_)
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ")
    
x = [notas]
y = [notas_n]

plt.plot(x,y)
plt.show()
