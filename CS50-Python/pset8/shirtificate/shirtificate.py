# Mina Nilay TEZER

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        # Instantiation of inherited class
        self._pdf = FPDF()
        self._pdf.add_page()
        # Setting font: helvetica bold 25
        self._pdf.set_font("helvetica", "B", 25)
        # Printing title
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        # Randering tshirt image
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(15)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")


        self._pdf.output("shirtificate.pdf")



def main():
    name = input("Name: ")
    pdf = PDF(name)


if __name__ == "__main__":
    main()