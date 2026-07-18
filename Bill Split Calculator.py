print ("Bill Split Calculator")
bill_amount = float(input("Enter your bill amount: $"))
tip_percentage = float(input("Enter your tip percentage: "))
tip_amount = float(tip_percentage / 100) * float(bill_amount)
total_amount = (tip_amount) + (bill_amount)
print (f"Your total bill (including tip) is ${total_amount}")
no_of_people = float(input("Enter the no. of people: "))
per_person_split = total_amount / no_of_people
print (f"The per person split is ${per_person_split}")