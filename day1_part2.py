#examples list

lista=[+1,-2,+3,+1]
lista1=[+1,-1]
lista2=[+3,+3,+4,-2,-4]
lista3=[-6,+3,+8,+5,-6]
lista4=[+7,+7,-2,-7,-4]

#################################################################################################
listaResultats=[0]

FreqActual=0;  # CURRENT FREQUENCY

i=0  # index for the list elements



entrada=open('day1_part2_input.txt','r').read() # putting the text info  to string called entrada




entradaLista=entrada.split("\n")  # SPLIT THE STRING OF THE TEXT AND PASSING TO LIST called entradaLista

#print(type(entradaLista[5]))
# parsing elements of the list, from string to int
while len(entradaLista)>i:
    entradaLista[i] = int(entradaLista[i])
    i=i+1


#print(type(entradaLista[5]))

#print(lista1)
#print(lista2)
dondeBuscar=entradaLista # the name of the list where you gona use for search if frequency apears twice
#print(lista1)
#print(dondeBuscar)

#CanviFrequ=int(dondeBuscar[i])

#print(len(dondeBuscar))
noTrobat=True  # variable notFound=True, we repeat until we found

count=0

while noTrobat:
    while len(dondeBuscar) > i:
        
        CanviFrequ=dondeBuscar[i]

        resultat=FreqActual + CanviFrequ
        #print("FreqActual ",FreqActual,"; CanviFrequ",CanviFrequ, "resultat: ", resultat)
        FreqActual=resultat
        i=i+1
        if FreqActual not in listaResultats:
           # print("no esta")
            listaResultats.append(FreqActual)
        elif FreqActual in listaResultats:
            print("First reaches ",FreqActual, "twice")
            noTrobat=False
            break

    #print("fi while!!!!!!!!!!!")
    #print(count)
    count = count+1
    i=0


#print("he fet el while",count, "vegades")

