import matplotlib.pyplot as plt  # as 'plt' apelido

#principio simples:

# x = [1,2,3,4]
# y = [2,4,6,8]
# plt.plot(x,y)
# plt.show()

#principio colocando titulos e nomes aos eixos:
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
plt.plot(x, y, label="dados", linestyle=":", color="#AE14EB", lw = 1.0, marker = ">")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.axis(xmin = 0, xmax = 10, ymin = 0, ymax = 10) #parâmentros de escala dos eixos
plt.title("Titulo do meu gráfico")
plt.legend()
plt.show()
