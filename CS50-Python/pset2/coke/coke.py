# Mina Nilay TEZER

amount_due = 50


while amount_due > 0:

    print("Amount Due:", amount_due)

    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5 :
        amount_due -= coin

owed = 0

if (amount_due < 0):
    owed = owed - amount_due
    print("Change owed:", owed)

else:
    print("Change owed: 0")