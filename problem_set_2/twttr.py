resposta = str(input("Input: "))

for c in resposta: #verificar cada caracter no str
    if c.lower() in ['a', 'e', 'i', 'o', 'u']: #verificar se o caracter e igual a qualquer uma destas vogais tanto em forma maiuscula ou minuscula atraves do ".lower"
        print("", end="")
    else:
        print(c, end="")
print()
