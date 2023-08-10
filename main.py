import Bill
import Flatmate
import PdfReport

try:
    bill_amount = int(input("Hey user, enter the bill amount: "))
    period = input("What is the bill period? E.g December 2020: ")
    user = input("What is your name? ")
    user_duration = int(input(f"How many days did {user} stay in the house during the bill period? "))
    users_flatmate_name = input("What is the name of the other flatmate? ")
    flatmate_stay = int(input(f"How many days did {users_flatmate_name} stay in the house during the bill period? "))

except (ValueError, TypeError):
    print("Please try again you have entered an incorrect Value")

else:
    the_bill = Bill.Bill(bill_amount, period)
    flatmate_1 = Flatmate.Flatmate(user, user_duration)
    flatmate_2 = Flatmate.Flatmate(users_flatmate_name, flatmate_stay)

    print(f"{user} pays: {flatmate_1.pays(the_bill)}")
    print(f"{users_flatmate_name} pays: {flatmate_2.pays(the_bill)}")

    pdf = PdfReport.PdfReport("MyCurrentBills.pdf")
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.generate(flatmate_1, flatmate_2, the_bill)
