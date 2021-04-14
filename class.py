class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
    def python_class(self):
        option = int(input("which of the following do you want 1) food 2) clothing 3) entertainment \n"))
        if option == 1:
            print("==== YOU CAN MAKE DEPOSIT FOR FOOD ====")
            print("==== YOU CAN MAKE DEPOSIT FOR CLOTHING ====")
            print("==== YOU CAN MAKE DEPOSIT FOR ENTERTAINMENT ====")
        elif option == 2:
            print("==== YOU CAN MAKE WITHDRAWAL FOR FOOD ====")
            print("==== YOU CAN MAKE WITHDRAWAL FOR CLOTHING ====")
            print("==== YOU CAN MAKE WITHDRAWAL FOR ENTERTAINMENT ====")
        elif option == 3:
            print("==== YOU CAN CHECK YOUR BALANCE FOR FOOD ====")
            print("==== YOU CAN CHECK YOUR BALANCE FOR CLOTHING ====")
            print("==== YOU CAN CHECK YOUR BALANCE FOR ENTERTAINMENT ====")
        elif option == 4:
            print("==== YOU CAN TRANSFER TO FOOD ====")
            print("==== YOU CAN TRANSER TO CLOTHING ====")
            print("==== YOU CAN TRANSER TO ENTERTAINMENT ====")
        else:
            print("INVALID REQUEST")


r1 = Budget("rice", "agbada", "music")
r1.python_class()

    
