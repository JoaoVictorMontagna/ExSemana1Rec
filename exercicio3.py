#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista_aninhada):
    soma = 0
    for lista in lista_aninhada:
        soma += sum(lista)
    return soma

lista = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]

print(soma_dos_aninhados(lista))  # Output: 231
print(soma_dos_aninhados(outra_lista))  # Output: 23








# Teste a sua função aqui (caso ache necessário)











