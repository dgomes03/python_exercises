# Get inputs
price = input("How much was the meal? ").replace('$', '')  # Remove $ if present
tip = input("How much would you like to tip? ").replace('%', '')  # Remove % if present

# Convert to appropriate types
conv_price = float(price)  # Convert price to a float
conv_percent = int(tip)  # Convert tip to an integer (percentage)

# Calculate the tip amount
result = conv_price * (conv_percent / 100)  # Tip percentage applied to the price

# Print result
print(f"Tip amount: ${result:.2f}") #da print com 2 casas decimais
