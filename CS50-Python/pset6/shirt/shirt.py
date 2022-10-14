# Mina Nilay TEZER

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    take_argument()
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    extension_check(file1 , file2)
    open_and_resize(file1 , file2)

def take_argument():
    # We need to take 2 command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    return sys.argv[1],sys.argv[2]

def extension_check(file1, file2):
     # By using os.path.splitext we'll split our text from it's dot
    file_1 = splitext(file1)
    file_2 = splitext(file2)

    if take_extension(file_1[1]) == False:
        sys.exit("Invalid input")

    # We are using if because this is not a check a if it is not then check b situation
    # we must check both of the extentions
    if take_extension(file_2[1]) == False:
        sys.exit("Invalid output")

    if file_1[1].lower() != file_2[1].lower():
        sys.exit("Input and output have different extensions")

def take_extension(file):
    if file in [".jpg", ".jepg", ".png"]:
        return True
    return False

def open_and_resize(file1 , file2):

    try:
        image = Image.open(file1)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    size = shirt.size

    foto = ImageOps.fit(image, size)

    foto.paste(shirt, shirt)

    foto.save(file2)

if __name__ == "__main__":

    main()