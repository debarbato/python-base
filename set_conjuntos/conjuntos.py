# set Serve para pegar elementos unicos
fruta = "banana"
c1 = set(fruta)
print(c1)

conjunto_a = [1,2,3,4,5]
conjunto_b = [4,5,6,7,8]

# UNIAO
uniao = set(conjunto_a) | set(conjunto_b)
print("Uniao: ",uniao)

# INTERSECAO
conjunto_a = set([1,2,3,4,5])
conjunto_b = set([4,5,6,7,8])

intersecao = conjunto_a.intersection(conjunto_b)
print("intersecao ",intersecao)

intersecao2 = conjunto_a & conjunto_b
print("intersecao2 ", intersecao2)

# DIFERENCA
dif = conjunto_a - conjunto_b
print("diferenca: ", dif)

# DIFERENCA SIMETRICA => Pega so o que tem em A e em B
difs = conjunto_a.symmetric_difference(conjunto_b)
difs2 = conjunto_a ^ conjunto_b
print("DIFERENCA SIMETRICA: ", difs)
print("DIFERENCA SIMETRICA2: ", difs2)

# Hashe Table => mapa para saber onde esta o elemento e encontrar mais rapido 
# Diferente da operacao O(n) que percorre a lista inteira
n = [1,1,1,2,3,4,1,8,7]
print(n)
print("4 esta em n?", 4 in n)

n =set([1,1,1,2,3,4,1,8,7])
print("n setedo: ", n)

print("4 esta em n_setado?(encontra mais rapido)", 4 in n)












