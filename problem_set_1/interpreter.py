expression = input("Expression: ")

#separar cada componente atraves do " ".
x, y, z = expression.split(" ")

#exemplo: 4 + 2 --> x= 4, y= +, z = 2
#no entanto, isto e um string, portanto --> transformar x e z em float:
floatx = float(x)
floatz = float(z)

#calcular resultados
if y == "+":
    result = floatx + floatz

if y == "-":
    result = floatx - floatz

if y == "*":
    result = floatx * floatz

if y == "/":
    result = floatx / floatz

#queremos arredondar o resultado final a 1 casa decimal:
print(round(result, 1))

#NOTA: tambem e posivel usar "print("Tip amount:", round(result, 2))", mas o problema e que se o resultado for $10, o output vai ser $10 e nao $10.00.
