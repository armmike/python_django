#MUTABLES 2
'''

Definicion de diccionarios, acceso a los elementos, 
añadir nuevas claves y métodos.
Clave Inmutable: número, tsr, tuple


'''

d = { 'uno': 1, 'dos': 2,  'tres': 3}

print(len(d))

print(d['uno'])
d['uno'] = 100
print(d, type(d))

clases = {'lunes': ['C', 'C++'],
          'martes': ['PHP'],
          'miercoles': ['SqK','Python']}

for d, lang in clases.items():
    print(d, lang)

#.items devuelve tuplas, se suele usar en buscadores
    
print(clases['lunes'])
clases['jueves'] = ['PHP','Python']
#Añadir SQL al martes:
clases['martes'].append('SQL')
clases['miercoles'].clear()
print(clases)

dias = 'LMXJVSD'
numeros = list(range(1,8))
print(numeros)

d2 =dict(zip(dias, numeros))
print(d2)


d3 =dict(zip(numeros, dias))
print(d3)

d2['S'] = 6
print(d2)

#claves 
print(list(d3.keys()))

print(d3[3])

#manejo de errores en diccionarios
try:
    # Acceso a una clave que no existe
    print(d3[30])
except Exception as e:
    print('Error: ',e)

#Es recomendable hacerlo como un bloque
#Siempre se aborta.

print('fin')

#range() se usa para hacer iteraciones sin 
#iteralble(colecciones) range(ini, fin-1, salto = 1), EL SALTO PUEDE SER NEGATIVO
#list() crea una lista con lo de dentro.

#zip() Se usa para intercalar diccionarios, en caso de que cambie la longitud
# elige el más corto.

#Ahí clases martes representa su valor, es decir, la lista ['PHP']

#dir(list) : métodos para las listas
