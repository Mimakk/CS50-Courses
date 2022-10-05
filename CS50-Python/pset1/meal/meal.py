# Mina Nilay TEZER

def main():
    answer = input("What time is it? ")

    time = convert(answer)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if time.endswith("a.m."):
        time, am = time.split(" ")
        hours, minutes = time.split(":")
    elif time.endswith("p.m."):
        time, pm = time.split(" ")
        hours, minutes = time.split(":")
        hours = float(hours) + 12
    else:
        hours, minutes = time.split(":")

    new_minute = float(minutes) / 60
    # 1 hour     60 minutes
    # x hour     30 minutes
    #----------------------
    # x*60 = 1*30 --->  x = 30 / 60
    # so minute / 60 is our new minute

    return float(hours) + new_minute


if __name__ == "__main__":
    main()