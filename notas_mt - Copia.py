import matplotlib.pyplot as plt

# lista = [1,1,1,2,3,4,5]




lista_notas = []
y = []
cont1 = 0 
cont2 = 0
cont3 = 0
cont4 = 0   
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0
cont10 = 0


def notas(i):
    if i == 1:
        cont1 = x
        return cont1
    elif i == 2:
        cont2 = x
        return cont2
    elif i == 3:
        cont3 = x
        return cont3
    elif i == 4:
        cont4 = x
        return cont4
    elif i == 5:
        cont5 = x
        return cont5
    elif i == 6:
        cont6 = x
        return cont6
    elif i == 7:
        cont7 = x
        return cont7
    elif i == 8:
        cont8 = x
        return cont8
    elif i == 9:
        cont9 = x
        return cont9
    elif i == 10:
        cont10 = x
        return cont10

repetir = "sim"
while repetir == "sim":
    lista_notas.append(int(input("Digite aqui a nota do aluno: ")))
    repetir = input("'sim' ou 'não': ")

for i in lista_notas:
    x = lista_notas.count(i)
    if i == 1:
        cont1 = x
    
    elif i == 2:
        cont2 = x
    
    elif i == 3:
        cont3 = x
    
    elif i == 4:
        cont4 = x
    
    elif i == 5:
        cont5 = x
    
    elif i == 6:
        cont6 = x
    
    elif i == 7:
        cont7 = x
    
    elif i == 8:
        cont8 = x
    
    elif i == 9:
        cont9 = x
    
    elif i == 10:
        cont10 = x

y.append((cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10))
print(y)

plt.plot(lista_notas,y, label = "dados")
plt.title("notas dos alunos")
plt.legend()
plt.xlabel("notas")
plt.ylabel("quantidade")
plt.show()



