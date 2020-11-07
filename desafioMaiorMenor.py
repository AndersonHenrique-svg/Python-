numeros = [] #lista com os numeros

for num in range(100): #loop pra receber e salvar os numeros na lista
    num = int(input())
    if num == 0:
        break
    elif num >= 1:
        numeros.append(num) # é aqui o metodo de adicionar na lista
    
print(max(numeros))# printa o numero maior