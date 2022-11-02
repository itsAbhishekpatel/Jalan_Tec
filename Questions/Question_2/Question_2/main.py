
class CoffeHouse:
    def __init__(self,milk,cream,latte):
        self.Milk = milk
        self.Cream = cream
        self.Latte = latte

    @staticmethod 
    def display():
        print("List of Coffee avalable:\n")
        print("1.Expresso / Milk, Cream, Latte having price 60, 75, 100 respectivly.")
        print("2.Cappuccino / Milk, Cream, Latte having price 80, 90, 125 respectivly.")
        print("3.Latte / Milk, Cream, Latte having price 100, 125, 150 respectivly.")

    @staticmethod 
    def choose():
        print("CHOOSE YOUR COFFE TYPE.")
        choose = int(input("Enter 1 for Expresso.\n Enter 2 for Cappuccino.\n Enter 3 for Latte."))
        print("PREFERRED ADD-ON IS?")
        add_on = int(input(" Enter 1 for Milk\n Enter 2 for Cream \nEnter  3 for Latte.") )
        return choose,add_on

      
Espresso = CoffeHouse(60,75,100)
Cappuccino = CoffeHouse(80,90,125)
Latte = CoffeHouse(100,125,150)


def bill():
        choose, add_on = CoffeHouse.choose()
        product = {1:{1:Espresso.Milk,2:Espresso.Cream,3:Espresso.Latte},
                   2:{1:Cappuccino.Milk,2:Cappuccino.Cream,3:Cappuccino.Latte},
                   3:{1:Latte.Milk,2:Latte.Cream,3:Latte.Latte} }
        return product[choose][add_on]
        r
def main():
    flag = True
    price = 0 
    CoffeHouse.display()       
    while flag :    

        price += bill()
        id = input("Do you want to order something else?(Y/N)")
        if id == "N":
            flag = False

    print(f"Total Price :{price}")

main()
