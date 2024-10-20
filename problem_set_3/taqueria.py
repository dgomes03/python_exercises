def main():
    money = 0
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    while True:
        try:
            order = input("Item: ").title()
            if order in menu:
                money += menu[order]
                print("Total: $",f"{money:.2f}", sep="")
        except:
            return main

main()
