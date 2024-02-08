#INMUTABLES 1
'''
Tuplas 
Creación y manejo
    - iNICIALIZAR MÚLTIPLES
    - Intercambiar variables
    Variable con asterisco delante FUNCIONES: TUPLA
    DOS DICCIONARIO
'''

t1 = 1,2,3,4, #Tupla sin parentesis con posibilidad de ampliación
t2 = (1,2,3,4)

print(t1, type(t1))
print(t2, type(t2))

t3 = (4,) # Se deja puesta si creas una tupla con un elemento la coma indica que es una tupla
#Se usan en Dujango para añadir apliaciones por ejemplo

frase = 'Hola que tal'
t = tuple(frase)
print(t)
#NO deja modificarla
#error type error
try:
    t[0] = 'x'
except Exception as e: #type error
    print(e)

print('Primer espacio: ', t.index(' ')) #index si no encuentra lanza error ValueError
print('Segundo espacio: ', t.index(' ',5)) 
#Concatenar, multiplicar 
#.count() e .index()[Primera posición que ocupa el carácter en la tupla]
#help(tuple.index)
'''
index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.

    Raises ValueError if the value is not present.
'''

#Buscar  en strigs y tuples

frase = 'h h h h h h h'
n = frase.count(' ')
print(n)
#For ideal: colección o saber cuantas veces
inicio = 0
for i in range(n):
    pos = frase.index(' ',inicio) #no puedes hacer pos+1 dentro en PYTHON
    print('pos espacio', pos)
    inicio = pos + 1

#Aparecen en inicializaciones.  
#Valores que no se van a modificar, así vienen los datos de una BBDD

L = [('Ana', 23, 1.3),('Anad', 233, 1.32),('sAna', 232, 1.31),]   
#Expansión de tuplas
for nom, age, alt in L:
    print(nom, 'hola', age, alt)

#Pones tanta variables como elementos en la tupla
#FIN INMUTABLES

