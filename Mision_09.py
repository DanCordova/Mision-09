#Autor: Daniel Córdova Bermúdez
#Grupo: 02
#Mision 09: La mision 9 consiste de funciones donde se usan listas para obtenter un resultado desado.


#Función extraer pares sirve para imprimir una nueva lista solamente los numero de una lista que son pares.
def extraerPares(lista):

    sinPares = []
    for numero in lista:
        if numero % 2 == 0:
            sinPares.append(numero)
    return sinPares


#Función extraerMayoresPrevio recibe una lista como parametro y regresa una lista nueva con los valores que son mayores a un elemento previo.
def extraerMayoresPrevio(lista):

    mayoresPrevio = []
    for numero in range(1,len(lista)):
        if lista[numero] > lista[numero-1]:
            mayoresPrevio.append(lista[numero])
    return mayoresPrevio


#La funcion cambia las parejas de una lista y regresa una nueva con las parejas intercambiadas.
def intercambiarParejas(lista):

    listaParejas = []
    n = len(lista)
    for numero in range(1, n, 2):
        listaParejas.append(lista[numero])
        listaParejas.append(lista[numero-1])
    if n % 2 == 1:
        listaParejas.append(lista[-1])
    return listaParejas

#La funcion recibe una lista que intercambia el numero mayor por el menor en la lista original.
def intercambiarMM(lista):

    if len(lista) > 1:
        minimo = min(lista)
        maximo = max(lista)
        menor = lista.index(minimo)
        mayor = lista.index(maximo)
        lista[menor], lista[mayor] = maximo, minimo

        return lista

    else:
        return lista


#Funcion promdiarCentro hace el promedio de una lista sin considerar el numero mayor y menor.
def promediarCentro(lista):

    listaOrdenada = lista
    listaOrdenada.sort()
    n = len(listaOrdenada)

    listaFinal = listaOrdenada[1:n-1]
    if n > 2:
        promedio = sum(listaFinal)//len(listaFinal)
        return promedio
    else:
        return 0


#Recibe una lista la cual debe calcular la media y la desviacion.
def calcularEstadistica(lista):

     n=len(lista)
     if n > 1:
         media = sum(lista)/n

     else:
         media = 0

     if n > 1:
         suma = 0
         for numero in lista:
             suma += (numero-media)**2
         desviacion = ((suma / (n - 1))) ** 0.5

     else:
         desviacion = 0



     dupla = (media, desviacion)

     return dupla




