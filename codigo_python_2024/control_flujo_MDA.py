'''
Bucles: for, while

Cndiciones: if else, if compacto
break y continue
romper bucles y saltar iteraciones

'''
#Bucle for anidados para imprimir matriz
M = [[1,3,4],[4,5,6],[7,8,9]]

for i in M:
    print(i)

for fila in M:
    for i in fila:
        print(i, end = '\t')
    print() #Para tener formato de matriz, salto de línea
#\t tabulador horizontal
#Evitar salto de linea en print

#while dados 2 numeros comprobar si son iguales
n1 = 10
n2 = 20

if n1 < n2: 
    print('El menor es ', n1)
elif n1 == n2:
    print('Son iguales')
else: 
    print('El mayor es: ', n1)

#If compacto\
n = 23
print('par' if n % 2 == 0 else 'impar')

n1 = 2
n2 = 1

menor = n1 if n1 < n2 else n2
print(menor)
