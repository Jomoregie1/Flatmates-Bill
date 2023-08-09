class Bill:
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period

class Flatmate:

    def __init__(self, name,    days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass

class PdfReport:

    def __int__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        pass