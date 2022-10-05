# Mina Nilay TEZER

# List of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Forever loop
while True:
    # Take input from user
    date = input("Date: ").strip()

    try:
        # Split date by /
        month, day, year = date.split("/")

        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break

    except:
        try:
            old_month , old_day, year = date.split(" ")
            # To find the number of the month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1

            if not old_day.endswith(","):
                continue

            day = old_day.replace(",","")

            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break

        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")