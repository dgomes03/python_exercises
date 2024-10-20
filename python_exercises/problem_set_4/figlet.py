import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()

#verificar o tamanho do codigo de execucao. se for ==1 entao quer dizer que o user nao pediu nenhuma font especifica
if len(sys.argv) == 1:
    #utilizamos funcao isRandom para mais a frente escolhermos font ao acaso.
    isRandom = True
#verificar o tamanho do codigo de execucao. se for ==3 entao quer dizer que o user pediu font especifica
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandom = False
#caso a estrutura seja diferente, entao sair do programa
else:
    print("Invalid Usage")
    sys.exit(1)
#agora vamos definir o que acontece quando a funcao isRandom toma valores V e F
if isRandom == False:
    try:
        figlet.setFont(font=sys.argv[-1])
    except:
        #caso nao seja possivel encontrar essa font, entao:
        print("Invalid usage")
        sys.exit(1)
else:
    #para casos em que isRandom == True:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)

user = input("Input: ")
print(figlet.renderText(user))
