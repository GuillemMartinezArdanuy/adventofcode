#entrada=input("ingrese lista, separados por coma, por ejemplo +1,+1,-2")
entrada=open('day1_input.txt','r').read()
#print(entrada)
entradaLista=entrada.split("\n")  # la string del usuario la pasamos a lista, separando por  caracter --->  ,
#print(entradaLista[1])
sumaEntrada=0  # valor de entradas  SERA EL VALOR DE CHANGE OF
i=0  # para recorrer la lista



tamanyLista=len(entradaLista)

#print(entradaLista[3])

#print("tamany lista",tamanyLista)

while tamanyLista > i:
    #print("index",i)
    sumaEntrada = sumaEntrada+int(entradaLista[i])  # casteamos a int
    #print("sumaEntrada",sumaEntrada)
    i = i+1

print(sumaEntrada)


