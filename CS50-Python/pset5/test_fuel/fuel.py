def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x , y = fraction.split('/')
            X = int(x)
            Y = int(y)
            result = X / Y
            if result <= 1:
                p = int(result * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ZeroDivisionError, ValueError):
            raise



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


