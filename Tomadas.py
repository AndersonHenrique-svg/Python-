
#Separar os valores em uma lista e converter para 'int';
valores = input().split()
lista_numeros = []
for x in valores:
    lista_numeros.append(int(x))

#Calculando o resultado através da soma dos valores da lista e subtraindo pelo tamanho da lista;
    #O tamanho da lista foi subtrído por -1 porque a ultima tomada não está conectada a outra;
resultado =  sum(lista_numeros) - ((len(lista_numeros))-1)

#Total de tomadas disponíveis;
#Esse resultado foi calculado considerando que cada régua de tomada esta conectada em outra;
print(resultado)




