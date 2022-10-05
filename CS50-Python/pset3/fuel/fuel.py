# Mina Nilay TEZER

while True:
    fuel = input("Fraction: ")
    try:
        x , y = fuel.split('/')
        X = int(x)
        Y = int(y)
        result = X / Y
        if result <= 1:
            break
    except (ZeroDivisionError, ValueError):
        pass
final_result = int(result * 100)

if final_result <= 1:
    print("E")
elif final_result >= 99:
    print("F")
else:
    print(f"{final_result}%")