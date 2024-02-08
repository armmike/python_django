#MUTABLES 1
""" 
Listas Objetos Mutables

"""

eje1 = ['Nombre','Nombre2','Nombre3','Nombre4','Nombre5','Nombre6']

#Índices positivos [0 - x]
#Índices neg [-x - -1]
print('-'*50)
print(eje1[2], eje1[4])
print('-'*50)
print(eje1[-1], eje1[5])
print('-'*50)
#Slicing: listas, cadeas, tuplas
# eje[ini:fin-1:salto=1]
print('-'*50)
print(eje1)
print('-'*50)
print('Los tres primeros ', eje1[1:3], eje1[:3])
print('-'*50)
print('Los 3 últimos: ', eje1[-3:])
print('-'*50)
print('quitar primero y último: ', eje1[1:-1])
print('-'*50)

#Bucle FOR, in, +. *
print('fOR NORMAL')
print('-'*50)
for i in eje1:
    print(i)

print('ENUMERATE')

print('-'*50)

for pos, i in enumerate(eje1):
    print(pos, i)
    
print('-'*50)

#{Puedes comprobar con in si un elemento está en una lista}\
#Diccionarios? Default en las claves, si quieres valores tienes
#que hacerlo en VALUES
#Posicion lista.index(elemento de la lista)

#Concatenar listas
L2 = [1,23,34,53,563]
print('-'*50)
L4 = eje1 + L2
print('-'*50)
print(eje1)
print('-'*50)
print(L2)
print('-'*50)
print(L4)
print('-'*50)
print(eje1 + L2)
print('-'*50)
print(eje1 * 4)
print('-'*50)
# + funciona igual en cadenas, tuplas, listas
# * concatena x veces la lista