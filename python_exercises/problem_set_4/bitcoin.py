import requests
import sys
import json

if len(sys.argv) == 2:
    try:
        buy = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
result = response.json()
price = result["bpi"]["USD"]["rate_float"]
total = price * buy
print(f"${total:,.4f}")
