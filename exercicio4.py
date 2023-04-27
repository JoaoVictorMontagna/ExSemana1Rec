#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui




def tem_duplicados (lista):
    nr=[]
    for i in lista:
        if lista.count(i)>1:
            nr.append(i)

    novalista=set(nr)
    tem=len(novalista)
    if tem>0:
        return True
    else:
        return False 
 

print(tem_duplicados([1,2,3,4,4]))



# Teste a sua função aqui (caso ache necessário)











