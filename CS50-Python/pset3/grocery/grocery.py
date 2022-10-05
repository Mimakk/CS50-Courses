# Mina Nilay TEZER

# Create an ampty dictionary
grocery = {}
# Loop forever
while True:
    try:
        # Get user input
        item = input().lower()
        # Check if item is already in dictionary
        if item in grocery:
            # If it is, add 1 in the count
            grocery[item] += 1
        # Otherwise add item for the first time
        else:
            grocery[item] = 1

    except EOFError:
        # Print all the item in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())

        # Stop the while loop
        break