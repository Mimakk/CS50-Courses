# Mina N. TEZER

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

if len(sys.argv) == 1:
    # To print some random font
    font = random.choice(figlet.getFonts())

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
     # To print some specify font
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)

else:
    print("Invalid usage")
    sys.exit(1)

msg = input("Input: ")

print("Output: ")
print(figlet.renderText(msg))






