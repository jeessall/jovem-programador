set1={1,2,3}
set2={3,4,5}
diferenca=set1.difference(set2)
print(diferenca)

numeros={1,2,3}
print("Set original:", numeros)
#Adicionando elementos
numeros.add(4)
print("Após add:", numeros)
#Removendo elementos
numeros.remove(2)
print("Após remover", numeros)

set1={1,2,3}
set2={3,4,5}
uniao=set1.union(set2)
print(uniao)

set1={1,2,3}
set2={3,4,5}
intersecao=set1.intersection(set2)
print(intersecao)

set1={1,2,3}
set2={3,4,5}
diferenca=set1.difference(set2)
print(diferenca)
#set1-set2

set1={1,2,3}
set2={3,4,5}
dif_simetrica=set1.symmetric_difference(set2)
print(dif_simetrica)