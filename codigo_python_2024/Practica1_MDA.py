#MUTABLES 4
'''
Cargar el texto del fichero: Contenido.txt
Generar un histograma que nos muestra el número
de veces que se repite cada palabra en texto

'''


#Cargar el fichero:

fich = open('/home/pipomk/Documents/python_django/codigo_python_2024/Contenido.txt', 'r')

#Si no existe hay una excepcion, FileNotFounError

txt = fich.read()
fich.close()

txt = txt.replace(',', '').replace('.','').replace(';', '').replace(':','')
#replace() lo que quiero buscar y por lo que lo quiero reemplazar

#s.split(' '), separa en lista de palabras
#L.count(2) te dice el numero de veces que está el 2

print(txt)
palabras = txt.split(' ')
print('num palabras', len(palabras))

#Conjunto sin repeticiones

palabrasSinRep = set(palabras)
print('num sin rep:', len(palabrasSinRep))

print('FINAL')

histograma = dict()

for i in palabrasSinRep:
    histograma[i] = palabras.count(i)

print(histograma)

#MUTABLES FIN

