#Vending Machine Practice

#Select Drinks
def select():
    global selection
    selection = input("A) Coke, B) Sprite")
    
#Customer's option
def options():
    global price
    global bill
    if selection == "A" or selection == "a":
        print("You chose Coke, $1.99")
        price = 1.99
        bill = float(input("Insert bill: "))
    elif selection == "B" or selection == "b":
        print("You chose Sprite, $2.50")
        price = 2.5
        bill = float(input("Insert bill: "))
    else:
        print("Invalid choice")
        print("Please either choose A or B")
        select()
        options()
#Did not know how to use while look
#Called functions to repeat
select()
options()
if bill == price:
    print("No change")
elif bill > price:
    change = float(bill) - float(price)
    if change > 0:
        print("Take your change: $" + str(change))

elif bill != 0 and bill < price:
    change = float(bill) - float(price)
    print("Not enough Credit. Insert $" + str(abs(change)) + " more to purchase")
elif bill == 0:
    print("You didn't insert any amount.")
