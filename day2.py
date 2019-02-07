
def TwoAndThreeOccurrence(word):
    lletresParaula = []  # list where we add new letters
    i = 0
    dictLletresParaula = {}  # dict where key is the letter (char) , and value the number of appears
    while len(word)>i: # we search in all string
        if word[i] not in lletresParaula:  #if the char is not in the list of new letters, we add this new char, for example 'L' on list.
            lletresParaula.append(word[i])
            dictLletresParaula[word[i]]=1 # 1, cause is the first occurrence
            i=i+1 # increment of index for comparing next char
        else:
            dictLletresParaula[word[i]] = dictLletresParaula[word[i]] + 1 # sum 1 , cause is another occurrence
            i=i+1

    contain2=0;
    contain3=0;
    for i in dictLletresParaula:
       # print(type(dictLletresParaula[i]))
        if dictLletresParaula[i]==2:
            contain2=1  #only one  ,not more
        if dictLletresParaula[i]==3:
            contain3=1  # only one , not more

    return contain2,contain3



sumaContain2=0
sumaContain3=0


# now we parse the document of inputs puzzle to string
entrada=open('day2_input.txt','r').read()
# now we put the string into list of value
entradaLista=entrada.split("\n")
j=0 # index for entradaLista

while len(entradaLista)>j:
    stringToCount=entradaLista[j]
    TwoAndThreeOccurrence(stringToCount)
    sumaContain2=sumaContain2+TwoAndThreeOccurrence(stringToCount)[0]
    sumaContain3=sumaContain3+TwoAndThreeOccurrence(stringToCount)[1]
    j=j+1

checksum=sumaContain2*sumaContain3
print("sumacontain2: ",sumaContain2)
print("sumacontain3: ",sumaContain3)
print("checksum: ", checksum)

