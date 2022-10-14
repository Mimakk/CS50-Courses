# Mina N. TEZER

import random


def main():

    level = get_level()

    question = 0
    score = 0

    while question < 10:
        x,y = generate_integer(level)
        response = tries(x,y)
        if response == True:
            score += 1
        question += 1

    print(f"Score: {score}")



def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass

    return level

def generate_integer(level):

    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y

def tries(x,y):
    wrong_answer = 0
    while wrong_answer < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                wrong_answer += 1
                print("EEE")
        except:
            wrong_answer += 1
            print("EEE")

    print(f"{x} + {y} = {x+y}")

    return False

if __name__ == "__main__":
    main()
    