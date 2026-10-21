bill = float(input("Enter the bill amount: $"))

tip_percent = float(input("Enter tip percentage: "))

total_people = int(input("How many People splitting the bill? "))

tip = bill * tip_percent / 100

total = bill + tip


print(f"Tip amount: ${tip:.2f}")
print(f"Total amount: ${total:.2f}")

if total_people > 0:
    per_person = total / people
    print(f"Each person Owes : $ {per_person:.2f}")

else:
    print("Number of people must be greater than zero.")
