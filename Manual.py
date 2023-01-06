from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")


pdf.add_page()

pdf.set_font(family="Times", style="B", size=12,)
pdf.cell(w=0, h=12, txt="Chandra Swaroop Reddy", align="L", ln=1, border=0)

pdf.set_font(family="Arial", style="B", size=12,)
pdf.cell(w=0, h=12, txt="Chandra Swaroop Reddy", align="L", ln=1, border=0)

pdf.output("output.pdf")
