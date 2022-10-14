import inflect

p = inflect.engine()

names = []

while True:
    try:
        # Get user input
        name = input("Name: ")
        names.append(name)

    except EOFError:
        # Stop the while loop
        print()
        break


output = p.join(names)
print(f"Adieu, adieu, to {output}")