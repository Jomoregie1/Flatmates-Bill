class Flatmate:

    total_days_stayed = 0

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        Flatmate.total_days_stayed += days_in_house

    def pays(self, bill):

        amount = bill.amount
        total_days = Flatmate.total_days_stayed
        print(f"Debug: amount = {amount}, total_days = {total_days}, self.days_in_house = {self.days_in_house}")
        amount_to_pay = round((amount/total_days) * self.days_in_house, 2)
        print(f"Debug: amount_to_pay = {amount_to_pay}")

        return amount_to_pay



