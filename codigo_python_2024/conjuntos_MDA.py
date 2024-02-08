#MUTABLES 3
'''
Conjuntos en Python
- Quitar repetidos de una lista
NO SE INDEXA, se recorre

set()
{}

'''

c = {1,3,2,2,2,1,1,1,4,5,6,8}
print(c, type(c))

#No es seguro que los de ordenados

#Quiutar repetidos de una lista
L = [1,2,3] * 4 

print(L)
L2 = list(set(L))
print(L2)

#Se pueden usar para comprobar si dos listas tienen elementos 
#en común: INTERSECCION &

p1 = ['espanol','ingles','frances']
p2 = ['aleman','ingles', 'frances']

c1 = set(p1)
c2 = set(p2)

print('idiomas comunes', c1 & c2)

#resta de conjuntos
print('idiomas que estan en 1 y no en 2: ', c1 - c2)
print('idiomas que estan en 1 y no en 2: ', c2 - c1)
#esto es el INNER JOIN(2) y el LEFT JOIN(1) de SQL

#UNION |
print('ambas:', c1 | c2)



