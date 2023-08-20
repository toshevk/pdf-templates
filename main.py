from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for page in range(row["Pages"]):
        pdf.add_page()

        if page == 0:
            # Set the header for first page of each topic
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=24, txt=row["Topic"], align="L", ln=1)
            pdf.line(x1=10, y1=27, x2=200, y2=27)

            # Set the footer for first page of each topic
            pdf.ln(250)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(200, 200, 200)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Set the footer for rest pages of topic
        pdf.ln(274)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(200, 200, 200)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
