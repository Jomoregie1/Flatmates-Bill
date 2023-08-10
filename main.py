import Bill
import Flatmate
import PdfReport

bill_amount = int(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g December 2020: ")
the_bill = Bill.Bill(bill_amount, period)

user = input("What is your name? ")
user_duration = input(f"How many days did {user} stay in the house during the bill period? ")
users_flatmate_name = input("What is the name of the other flatmate? ")
flatmate_stay = input(f"How many days did {users_flatmate_name} stay in the house during the bill period? ")

flatmate_1 = Flatmate.Flatmate(user, user_duration)
flatmate_2 = Flatmate.Flatmate(users_flatmate_name, flatmate_stay)

print(f"{user} pays: {flatmate_1.pays(the_bill)}")
print(f"{users_flatmate_name} pays: {flatmate_2.pays(the_bill)}")
