import inflect

names = []
p = inflect.engine()

while True:
    try:
        name = str(input("Input: "))
        names.append(name)
    except EOFError:
        print()
        break

result = p.join(names)
print("Adieu, adieu, to",result)
