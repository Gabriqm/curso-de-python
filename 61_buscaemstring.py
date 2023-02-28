frase = "Eu quero encontrar o peixe"

print(frase.find("peixe"))

if frase.find("peixe") >= 0:
    print("Encontrei o peixe")

print(frase.find("tubarão"))

if frase.find("tubarão") == -1:
    print("Não há tubarão na frase")
else:
    print("Há tubarão")