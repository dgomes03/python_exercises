def main():
    time = input("What time is it? ").strip() #strip de forma a retirar espacos a mais tanto antes como depois do str
    if 7.0 <= convert(time) <= 8.0: #aqui estamos a perguntar se o convert(time) que definimos abaixo se encontra entre estes intervalos.
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")
    else:
        return

#converter input em float no estilo "7.5", ou "20.2", etc.
def convert(time): #colocamos "time" uma vez que esta variavel vem de cima, sendo o input.
    x, y = time.split(":")
    hr = float(x)
    mins = float(y) * 1 / 60
    return float(hr+mins) #o que e que vamos enviar para funcao convert(time)? float(hr+mins)! por isso dizemos "return float(hr+mins)"


if __name__ == "__main__":
    main()
