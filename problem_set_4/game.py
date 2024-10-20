import random

while True:
    try:
        input = int(input("Level: "))
        if input > 0:
            break
    except:
        pass

random = random.randint(1,input)

while True:
    try:
        guess = int(input("Guess: "))
        if guess != 0:
            if guess < random:
                print("Too small!")
            elif guess > random:
                print("Too large!")
            else:
                print("Just Right!")
                break
    except:
        pass

#este exercicio nao funciona a 100%
