months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#iniciar loop para ir continuamente verificando o abaixo caso nao seja o que queremos
while True:
    date = input("Date: ")
    try:
        #verificar se a data inserida pelo user ta no formato de mm/dd/yyyy
        if "/" in date:
            #separar cada componente da data
            month, day, year = date.split("/")
            #verificar se o mes e dia estao enquadrados corretamente
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                #caso isto se verifique, entao podemos dar print e sair do loop (break)
                #tens de adicionar int pq senao e tratado como string
                print(f"{int(year)}", f"{int(month):02}", f"{int(day):02}", sep = "-")
                break
            #caso contrario levantar erro
            else:
                raise ValueError
        #verificar se input esta no formato month day, year
        elif "," in date:
            #separar componentes again
            monthday, year = date.split(", ")
            #separar o mes do dia
            month, day = monthday.split(" ")
            #ir buscar a lista dos meses o numero correspondente ao mes inserido, nao esquecer que listas comecam com 0, logo temos de fazer +1
            month = (months.index(month)) + 1
            #verificar que mes e dia estao bem enquadrados
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                #caso estejam, entao dar print do resultado e sair do loop
                print(f"{int(year)}", f"{int(month):02}", f"{int(day):02}", sep = "-")
                break
            #caso contrario levantar erro
            else:
                raise ValueError
    #caso o que acontece acima nao seja executado, entao e pq aconteceu algum grave erro, portanto sendo assim levantamos varios erros ao mesmo tempo e desligamos o programa
    except (AttributeError, ValueError, NameError, KeyError):
        pass
