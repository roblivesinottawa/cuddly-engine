print("Welcome to the tip calculator program.")

bill = float(input("what is the bill total? "))
tip = int(input("How much would you like to tip? 10%, 12%, or 15%? "))
guests = int(input("how many people are sharing the bill? "))

tip_perc = tip / 100
tip_amt = bill * tip_perc
total = bill + tip_amt
bill_guest = total / guests
final = round(bill_guest, 2)

print(f"the total per guest is: {final}")