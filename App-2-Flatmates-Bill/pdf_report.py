from fpdf import FPDF
import os
from bill import Bill
import webbrowser
os.makedirs('pdf', exist_ok=True)


class PdfReport:
    """Class to generate a PDF report for the bill.
    Attributes:
        filename (str): The name of the PDF file to be generated.
    """

    def __init__(self, bill):
        self.filename = bill.period.replace(" ", "_") + "_bill.pdf"

    def generate(self, flatmates, bill: Bill):
        """Generate the PDF report.
        Args:
            flatmates (list[Flatmate]): All flatmates.
            bill (Bill): The bill to be reported.
        """

        table_header = ['Name', 'Num_days', 'Need_to_pay', 'Total']
        data = []
        for flatmate in flatmates:
            data.append([
                flatmate.name,
                str(flatmate.days_in_house),
                f"${flatmate.pays(bill, flatmates)}",
                f"${bill.amount}"
            ])

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.add_page()

        # add icon
        pdf.image('files/house.png', x=pdf.l_margin, y=pdf.t_margin, w=33)
        pdf.set_font('Times', 'B', 24)
        pdf.cell(page_width, 50, 'Flatmates Bill', ln=1, align='C')
        pdf.set_font('Times', '', 16)
        pdf.cell(0, 30, f'Period: {bill.period}', ln=1, align='C')
        pdf.set_font('Times', '', 14)
        pdf.cell(0, 20, f'Total Bill: ${bill.amount}', ln=1, align='L')

        for flatmate in flatmates:
            pdf.cell(
                0, 20, f'{flatmate.name} pays: ${flatmate.pays(bill, flatmates)}', ln=1, align='L')

        pdf.ln(40)
        pdf.set_font('Times', size=12)

        usable_width = pdf.w - pdf.l_margin - pdf.r_margin
        col_width = usable_width / len(table_header)
        row_height = 28

        for header in table_header:
            pdf.cell(col_width, row_height, header, border=1, align='C')
        pdf.ln(row_height)

        for row in data:
            for item in row:
                pdf.cell(col_width, row_height, str(item), border=1, align='C')
            pdf.ln(row_height)

        pdf.output(f'pdf/{self.filename}')
        webbrowser.open(
            f'pdf/{self.filename}')
        # f'F:/Dev/python/practice/App-2-Flatmates-Bill/pdf/{self.filename}'
