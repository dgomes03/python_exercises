camel = input("camelCase: ")
print("snake_case: ", end="")

for c in camel: #loop que verifica cada caracter do string
    if c.islower(): #se esse caracter for minusculo, entao print c
        print(c, end="")
    if c.isupper(): #se esse caracter for maiusculo, entao print "_" e substitui por minuscula
        print("_", c.lower(), end="", sep="")

print() #comando que apenas cria uma nova linha
