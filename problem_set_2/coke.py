#definir valores iniciais
price = 50
paid = 0
coin_range = [25, 10, 5]

#loop de forma a constantemente verificar pagamento
while price > 0: #se o price > 0, ou seja, se ainda n tivermos pago, entao:
    print("Amount Due:", price)
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in coin_range: #verificar se a moeda inserida corresponde a 25, 10 ou 5
        price = price - inserted_coin
        paid = paid + inserted_coin

#caso demasiado dinheiro seja inserido, avisar:
if paid >= price:
    print("Change Owed:", paid - 50)
