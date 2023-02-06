#tuplas são listas com dados imutáveis.

tupla = (1,2,3)

print(tupla)

print(type(tupla))

print(tupla[0])

#para iterar em tuplas, utilizamos o for:

tupla2 = ("Gabriel", "Maria", "Zé")

for nome in tupla2:
    print(nome)

    if nome == "Gabriel":
        print("Parabéns Gabriel")

i = 0

while i < len(tupla2):
    print(tupla2[i])
    i = i + 1