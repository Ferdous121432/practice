import os
import webbrowser
from fpdf import FPDF


os.makedirs('pdf', exist_ok=True)

table_header = ['Name', 'Num_days', 'Need_to_pay', 'Total']
data = [
    ['Alice', '20', '$60', '$100'],
    ['Bob', '10', '$40', '$100']
]

pdf = FPDF(
    orientation='P',
    unit='pt',
    format='A4'
)
page_width = pdf.w - 2 * pdf.l_margin
pdf.add_page()

pdf.set_font('Times', 'B', 24)
pdf.image('files/house.png', x=pdf.l_margin, y=pdf.t_margin, w=24)
pdf.cell(page_width, 50, 'Flatmates Bill', ln=1, align='C')
pdf.set_font('Times', '', 16)
pdf.cell(0, 30, 'Period: March 2021', ln=1, align='C')
pdf.set_font('Times', '', 14)
pdf.cell(0, 20, 'Total Bill: $100', ln=1, align='L')
pdf.cell(0, 20, 'Alice pays: $60', ln=1, align='L')
pdf.cell(0, 20, 'Bob pays: $40', ln=1, align='L')
pdf.ln(40)
pdf.set_font('Times', size=12)

usable_width = pdf.w - pdf.l_margin - pdf.r_margin
col_width = usable_width / 4
row_height = 28

for r in range(1):
    for c in range(4):
        pdf.cell(col_width, row_height,
                 f'{table_header[c]}', border=1, align='C')
    pdf.ln(row_height)

for row in data:
    for item in row:
        pdf.cell(col_width, row_height,
                 f'{item}', border=1, align='C')
    pdf.ln(row_height)
pdf.output('pdf/hello-qq.pdf')
webbrowser.open('F:/Dev/python/practice/App-2-Flatmates-Bill/pdf/hello-qq.pdf')
print("PDF generated successfully: pdf/hello-qq.pdf")
