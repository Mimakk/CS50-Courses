# Mina N. TEZER

import json
import sys
import requests

def main ():

    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        money = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = r.json()
        bitcoin = response['bpi']['USD']['rate_float']
        in_dollar = money * bitcoin
        print(f"${in_dollar:,.4f}")

    except requests.RequestException:
        print("Request Exception")
        sys.exit(1)


if __name__ == "__main__":
    main()





