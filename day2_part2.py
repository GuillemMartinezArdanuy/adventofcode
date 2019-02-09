list1 = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz', 'pqrst']

'''
entrada=open('day2_input.txt','r').read()
# now we put the string into list of value
list13=entrada.split("\n")
'''

def crearListaCaractersColumnaFixa(nomLlista,columnaFixada):
    l_C_C = []  # llista de caracters de la columna
    llista=nomLlista
    columnaFixe=columnaFixada
    for paraula in llista:
        if paraula[columnaFixe] not in l_C_C:
            l_C_C.append(paraula[columnaFixe])

    #print(l_C_C)
    return l_C_C

#creem Lista de tots els caractersdelacolumna fixa:

def crearListaTotesLletresColumnaFixa(nomLlista,columnaFixada):
    l_T_L_C = []  # String de lletres de la columna
    llista=nomLlista
    columnaFixe=columnaFixada
    for paraula in llista:
        l_T_L_C.append(paraula[columnaFixe])

    #print("lista totes les lletres de la columna",l_T_L_C)
    return l_T_L_C


columnaFixa=0
ll_C_C=crearListaCaractersColumnaFixa(list1,columnaFixa)
l_T_Ll_C=crearListaTotesLletresColumnaFixa(list1,columnaFixa)
auxiliar_l_T_Ll_C=crearListaTotesLletresColumnaFixa(list1,columnaFixa)


res_l_P_F=[]

p_C=0 # guardem primera coincidencia
for paraula in list1:
    if paraula[columnaFixa] in l_T_Ll_C:
        #print(paraula[columnaFixa])
       # print("index: ",l_T_Ll_C.index(paraula[columnaFixa]))
        res_l_P_F.append(l_T_Ll_C.index(paraula[columnaFixa]))


    else:
        print("err")


## sino esta en la lista ,ponemos el valor a null
# despres tots els que no estan nuls, els posem a 1
listaBuida=[]




def listaZerosUns(columna):
    columnaFixa=columna
    l_T_Ll_C = crearListaTotesLletresColumnaFixa(list1, columnaFixa)
    auxiliar_l_T_Ll_C = crearListaTotesLletresColumnaFixa(list1, columnaFixa)
    for paraula in l_T_Ll_C: ## creo lista auxiliar, si eliminio auxiliar i comparo, i sigue la letra, significa que esta repetida, marco, con un 1, sino marco con un 0
        #print ("paraula--",paraula ,"posicio++:", l_T_Ll_C.index(paraula))
        auxiliar_l_T_Ll_C.remove(paraula)
        if paraula in auxiliar_l_T_Ll_C:
            #print("esta  poso 1 a  llista buida")
            listaBuida.append(1)
            #print("lsitabuida", listaBuida)
            #print("l_T_Ll_C:", l_T_Ll_C)
            auxiliar_l_T_Ll_C.clear()
            auxiliar_l_T_Ll_C = crearListaTotesLletresColumnaFixa(list1, columnaFixa)
            #print("auxiliar ----- DESPRES DE REINICIARLA---- lT_LL_C", auxiliar_l_T_Ll_C)

        else:
            #print("no esta poso 0 a llista buida")
            #print("l_T_Ll_C:", l_T_Ll_C)
            #print("auxiliar lT_LL_C", auxiliar_l_T_Ll_C)
            listaBuida.append(0)
            auxiliar_l_T_Ll_C.clear()
            auxiliar_l_T_Ll_C = crearListaTotesLletresColumnaFixa(list1, columnaFixa)

        #print(listaBuida)
    auxiliar_l_T_Ll_C.clear()
    return listaBuida






#print("l_T_Ll_C:",l_T_Ll_C)
#l_T_Ll_C.remove('a')
#print("l_T_Ll_C: --------- despres de eliminar a ",l_T_Ll_C)
#print("auxiliar lT_LL_C",auxiliar_l_T_Ll_C)
#print("resultat",res_l_P_F)
#print("lsitabuida",listaBuida)
#print("TAAAAAAAAAAAAACHAAAAAAAAAAAAAAAAAN!!!!!",listaZerosUns(0))






i=1
listaAuxiliar=listaZerosUns(0)
print(listaAuxiliar)
listaBuida.clear()

listaSuma=[]

listaResultats=[]

'''
while len(listaAuxiliar)>i:

    listaSuma.append(listaAuxiliar[i-1]+listaAuxiliar[i])
    i+=1

#
'''











#columnaFixa=0
#columnaFixa=int(input("columna a fixar?"))
#crearListaCaractersColumnaFixa(list1,columnaFixa)



