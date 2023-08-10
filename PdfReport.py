from fpdf import FPDF


class PdfReport(FPDF):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def header(self) -> None:
        self.image('files/house.png')
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'House Bill', 1, 0, 'C')
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def generate(self, flatmate1, flatmate2, bill):
        self.set_font('Times', 'B', 15)
        self.cell(0, 10, 'Period: ' + bill.period, 0, 1)
        self.set_font('Times', '', 12)
        self.cell(0, 10, f'Flatmate 1 (Total) - {flatmate1.name}: {flatmate1.pays(bill)}', align='L')
        self.ln()
        self.cell(0, 10, f'Flatmate 2 (Total) - {flatmate2.name}: {flatmate2.pays(bill)}', align='L', ln=1)
        self.output(self.filename)
