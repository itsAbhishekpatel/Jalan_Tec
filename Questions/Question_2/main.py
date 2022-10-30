
def display():
    print("List of Coffee avalable:\n")
    print("1.Expresso / Milk, Cream, Latte having price 60, 75, 100 respectivly.")
    print("2.Cappuccino / Milk, Cream, Latte having price 80, 90, 125 respectivly.")
    print("3.Latte / Milk, Cream, Latte having price 100, 125, 150 respectivly.")

def choose():
    choose = int(input("\nChoose your Coffee type:\n Enter 1 for Expresso.\n Enter 2 for Cappuccino.\n Enter 3 for Latte. "))
    add_on = int(input("\nPreferred add-on is?\n Enter 1 for Milk.\n Enter 2 for Cream.\n Enter 3 for Latte."))

    # print(choose,add_on)
    return choose,add_on

def bill():
    coffee ,add_on =choose()
    coffee = coffee-1
    add_on = add_on-1
    cost = [[60,75,100],[80,90,125],[100,125,150]]

    price = cost[coffee][add_on]
    return price

flag = True
order_value = 0

display()
while flag:    
    order_value += bill()
    order = input("You want to order again?(Y/N)")
    if order == "N" or "n" or "NO":
        flag = False

print(f"Total Price is : {order_value}")







