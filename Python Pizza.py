print("Welcome to the Python Pizza Delivery program!")
size = input("What size of pizza do you want? Input 'S' for small, 'M' for medium and 'L' for large: ").upper()

if size == "S":
    bill = 15
    print(f"You have selected the small pizza size, which costs ${bill}.")
elif size == "M":
    bill = 20
    print(f"You have selected the medium pizza size, which costs ${bill}.")
elif size == "L":
    bill = 25
    print(f"You have selected the large pizza size, which costs ${bill}.")
else:
    print("You have inputed an invaid response. You'll have to start again.") 
    
pepperoni = input("Do you want pepperoni on your pizza? This will cost an additional fee. Type 'Y' for yes and 'N' for no:  ").upper()
if pepperoni == "Y" and size == "S":
    bill += 2
    print(f"Your bill is ${bill}")
    
elif pepperoni == "Y" and size == "M" or size == "L":
    bill += 3
    print(f"Your bill is ${bill}")
    
cheese = input("Do you want cheese? This will cost an additional fee. Type 'Y' for yes and 'N' for no: ").upper()
if cheese == "Y":
    bill += 2
    print(f"Your total bill is ${bill}.")
elif cheese == "N":
    print(f"Alright! No cheese. Your total bill is ${bill}.") 
else:
    print("You have inputed an invaid response. You'll have to start again.")