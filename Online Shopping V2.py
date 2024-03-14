import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

def ShopperWRLD ():
    # Variables
    Cart = []
    loop = True
    z = 0

    # Item Quantity Generator

    r = round(random.random(), 2)
    stock = []
    if (z == 0):
        for n in range(80):
            R = round(100 * r)
            r = round(random.random(), 2)
            stock.append(R)

    # Store Dictionary
    Store = {
        1 :  {
            0: "Electronics and Technology",
            1: ['SAMSUNG 50" Class 4K Crystal UHD TV', stock[0], 397],
            2: ['EVOO 15.6" 2T Gaming Laptop', stock[1], 600],
            3: ["Black 32GB Samsung Galaxy A21", stock[2], 127],
            4: ["HP DeskJet 3772 Wireless Color Inkjet Printer", stock[3], 60],
            5: ["SAMSUNG Galaxy Buds+", stock[4], 100]},
        2 : {
            0: "Clothing, Shoes, and Accessories",
            1: ["Gucci Belt", stock[5], 1200],
            2: ["Supreme T-Shirt", stock[6], 38],
            3: ["Louis Vuitton Regular Denim Jeans", stock[7], 645],
            4: ["41 mm Hermes Arceau Chronographe Watch", stock[8], 5250],
            5: ["Hermes Collier de Chien Bracelet", stock[9], 49000]},
        3 : {
            0: "Toys and Games",
            1: ["LEGO Harry Potter Hogwarts Great Hall Set", stock[10], 89],
            2: ["LOL Surprise Tweens Fashion Doll Freshest", stock[11], 20],
            3: ["Super Smash Bros Ultimate", stock[12], 58],
            4: ["Beat Saber", stock[13], 30],
            5: ["Halo Infinite", stock[14], 60]},
        4 : {
            0: "Sports and Fitness",
            1: ["Umbro Soccer Ball", stock[15], 39],
            2: ['Spalding NBA Pro Tack 28.5" Basketball', stock[16], 18.46],
            3: ["Wilson NFL Super Grip Football ", stock[17], 26],
            4: ["5-25Lb Rubber Coated Hex Dumbbell Set", stock[18], 360],
            5: ["Abcnature 330lbs Weight Lifting Bench Multi Station", stock[19], 250]},
        5 : {
            0: "Beauty and Pharmaceutics",
            1: ["SHANY Carry All Trunk Makeup Set", stock[20], 45.49],
            2: ["Tylenol Cold + Flu Medicine Pack", stock[21], 6.48],
            3: ["Equate Antibacterial Assorted Bandages Variety Pack", stock[22], 6.67],
            4: ["Equate 70% Isopropyl Alcohol Antiseptic", stock[23], 2.18],
            5: ["Equate 91% Isopropyl Alcohol Antiseptic", stock[24], 2.78]},
        6 : {
            0: "Furniture",
            1: ["JOIVI Patio Furniture Set", stock[25], 500],
            2: ["Walnew Adjustable Armless Swivel Bar Stool", stock[26], 45],
            3: ["Full Bed Frame with Wooden Headboard and Bed Frame", stock[27], 180],
            4: ["Queen Bed with Metal Frame", stock[28], 192],
            5: ["King Bed with Bed Frame and Adjustable Headboard", stock[29], 220]},
        7: {
            0: "Pets",
            1: {
                0: "Dogs",
                1: ["FurHaven Small Dog Bed", stock[30], 21],
                2: ["FurHaven Medium Dog Bed", stock[31], 11.74],
                3: ["FurHaven Jumbo Dog Bed", stock[32], 13.49],
                4: ["Adjustable Dog Collar and Leash Set", stock[33], 12],
                5: ["Purina Beggin' Strips Dog Treats", stock[34], 2.84]},
            2: {
                0: "Cats",
                1: ["Petmaker Igloo Pet Cat Bed", stock[35], 16],
                2: ["Deluxe Cat Scratching Post", stock[36], 20],
                3: ["Pet Comb Self Cleaning Brush", stock[37], 13],
                4: ["Purina Tidy Cats Clumping Cat Litter", stock[38], 16.48],
                5: ["Meow Mix Dry Cat Food", stock[39], 12.12]},
            3: {
                0: "Snakes",
                1: ['REPTI-ZOO Reptile Glass Terrarium, 20" x 12" x 10', stock[40], 80],
                2: ["50W Reptile Heat Lamp", stock[41], 24],
                3: ["Reptile Terraium Decor Set", stock[42], 69],
                4: ["Koyal Wholesale 3 Pc DIY Terrarium Filler Kit", stock[43], 17],
                5: ["Frozen Large Mouse, 10 Ct", stock[44], 22]},
            4: {
                0: "Lizards",
                1: ["Prevue Pet Products Small Hamster Haven", stock[45], 47.43],
                2: ["Higgins Sunburst Hamster Animal Food", stock[46], 15],
                3: ["Gargrow Super-Silent Hamster Exercise Wheels", stock[47], 10.12],
                4: ["AKDSteel Hamster Exercise Ball", stock[48], 8.09],
                5: ["SPRING PARK DIY Hamster Tubes", stock[49], 9.13]},
            5: {
                0: "Fish",
                1: ["AquaCulture 10 Gallon Aquarium", stock[50], 18.30],
                2: ["AquaCulture Aquarium Gravel, Rainbow, 2 lb.", stock[51], 3],
                3: ["AquaCulture Aquarium Gravel, AquaBlue, 2 lb.", stock[52], 2.45],
                4: ["Tetra TetraMin Tropical Flakes Fish Food, 1 oz.", stock[53], 4.23],
                5: ["GreenJoy 12 Pack Aquarium Fish Tank Decorations", stock[54], 15.88]}},
        8 : {
            0: "Food",
            1: {
                0: "Breakfast",
                1: ["Premium Breakfast Sausage Patties, 8 count", stock[55], 2.76],
                2: ["Great Value Extra Large White Eggs, 18 Ct", stock[56], 3.50],
                3: ["Aunt Jemima Original Complete Pancake & Waffle Mix, 32 oz", stock[57], 3],
                4: ["Reese's Puffs Cereal", stock[58], 3.23],
                5: ["Cinnamon Toast Crunch", stock[59], 2.23]},
            2: {
                0: "Lunch",
                1: ["Frozen Hot Pockets, 12 ct", stock[60], 12],
                2: ["Totinos Pizza Rolls, 130 ct", stock[61], 11],
                3: ["Great Value Frozen Mini Corn Dogs, 40ct", stock[62], 7],
                4: ["Ore-Ida Frozen Seasoned Tater Tots, 5lb", stock[63], 7.35],
                5: ["Great Value Frozen Chicken Nuggets, 32 oz", stock[64], 5.58]},
            3: {
                0: "Dinner",
                1: ["Beef Choice Angus Ribeye Steak", stock[65], 20.36],
                2: ["Mahatma Authentic Aromatic Jasmine White Rice 5 Lb", stock[66], 7.40],
                3: ["Russet Potatoes, 10 lb Bag", stock[67], 6],
                4: ["Barilla Fettuccine Pasta, 16 oz", stock[68], 1.90],
                5: ["Ragu Old World Style Traditional Sauce", stock[69], 3.42]},
            4: {
                0: "Desert",
                1: ["Chocolate Chip Cookies, 50 ct", stock[70], 5.80],
                2: ["Large Apple Fritters, 2ct", stock[71], 1.50],
                3: ['5" Chocolate Cake', stock[72], 6],
                4: ["Ben & Jerry's The Tonight Dough", stock[73], 4.50],
                5: ["Ben & Jerry's Chocolate Chip Cookie Dough Core Ice Cream", stock[74], 4.50]},
            5: {
                0: "Snacks",
                1: ["Doritos Spicy Sweet Chili Party Size", stock[75], 5],
                2: ["Doritos Spicy Nacho Party Size", stock[76], 5],
                3: ["Nabisco Classic Mix Variety Pack, 20ct", stock[77], 8.70],
                4: ["Welch's Mixed Fruit Snacks Family Size, 40ct", stock[78], 8.50],
                5: ["Little Debbie Star Crunch, 12ct", stock[79], 2.60]}}
        }

    Isles(Store, Cart)

    try:
        NumberofItems = len(Cart)
    except TypeError:
        None
    else:
        Processing(Cart, Store)

def Isles (Store, Cart):
    loop = True
    while(loop):
        Choice = input(Fore.LIGHTMAGENTA_EX + "Do you want to enter an isle or search for an item? S for Search or I for Isle: ")
        if(not(isinstance(Choice, str))):
            Error()
            continue

        Choice = Choice.upper()
        if(Choice[0] == 'S'):
            ItemSearch(Store)

        elif(Choice[0] == 'I'):
            break

        else:
            Error()

    while(loop):
        for x in Store.keys():
            print(Fore.RED + Style.DIM + f'{x} - {Store[x][0]}') # Displays Main Isles

        Isle = input(Fore. GREEN + "Which isle do you want to enter? Enter 0 to exit")
        try:
            Isle = int(Isle)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Error!, the value you entered was not a number. Please enter a number\n")
            #If user inputs something odd and may crash program, prevents it from crashing and displays error

        if (isinstance(Isle, int)):
            if (not Isle):
                return False
            elif (Isle >= 1 and Isle <= 8):
                print("")
                Items(Store, Isle, Cart)
                break
            elif (not (Isle >= 0 and Isle <= 8)):
                Error()

    return Cart


def Items (Store, Isle, Cart):
    loop = True
    #For Main Isles 1 - 6
    if (Isle < 7):
        while(loop):

            for x in Store[Isle].keys():
                if (x == 0):
                    continue
                print(Back.BLACK + Fore.BLUE + Style.DIM + f'{x} - {Store[Isle][x][0] : <60} - ${Store[Isle][x][2] : ^1} - Stock: {Store[Isle][x][1]}' + Back.RESET)
                #Displays Selected Isle

            item = input(Fore.GREEN + "Which item do you want? Enter 0 to exit")
            Result = ValueCheck(item, 5)

            if (Result == None or Result == 9):
                Error()
                continue
                #User entered negative or number greater than the number of Isles

            elif(Result == 0):
                break
                #User entered 0 to leave

            else:
                item = int(item)
                while(loop):
                    print(Back.BLACK + Fore.BLUE + Style.DIM + f'{item} - {Store[Isle][item][0] : <60} - ${Store[Isle][item][2] : ^1} - Stock: {Store[Isle][item][1]}' + Back.RESET)
                    # Displays selected item

                    amount = input(Fore.LIGHTGREEN_EX + Style.BRIGHT + "How many do you want? Enter 0 to exit")
                    Result = ValueCheck(amount, Store[Isle][item][1])

                    if (Result == None):
                        Error()
                        continue
                        #User tried to enter a negative number

                    elif(Result == 9):
                        print(Fore.RED + Style.BRIGHT + "Not Enough in Stock\n")
                        continue
                        #User tried to be greedy, not allowed

                    elif(Result == 0):
                        break
                        # User entered 0 to leave

                    else:
                        amount = int(amount)
                        if(Result):
                            Store[Isle][item][1] -= amount        #Removes stock amount
                            Cart.append([Store[Isle][item], amount, (Isle, item)])      #Adds Selected item to cart and item information

                            while (loop):
                                #Keeps user in a loop to give correct input
                                leave = input(Fore.GREEN + "Do you want another item here? Enter Yes or No").upper()
                                if (not(isinstance(leave[0], str))):
                                    #Just Checks if it is a integer
                                    Error()
                                    continue

                                Result = ValueCheck(leave, None)
                                if (Result == -9 or Result == None):
                                    Error()
                                    continue
                                else:
                                    loop = False

            if (Result):
                loop = True

        if (not(Result)):
            while (True):
                leave2 = input(Fore.GREEN + Style.DIM + "Do you want to go back to the main isles or quit? M for Main Isles, Q for Quit: ").upper()
                if (not(isinstance(leave2[0], str))):
                    Error()
                    continue

                Result = ValueCheck(leave2, None)
                if (Result == -9 or Result == None):
                    Error()
                    continue
                else:
                    break

        try:
            if (Result):
                Isles(Store, Cart)
                #breaks out the Main Isle loop once recurision ends
        except UnboundLocalError:
            None
    
    #For Isles 7 and 8 with SubIsles
    else:
        while (loop):
            for x in Store[Isle].keys():
                if (x == 0):
                    continue
                print(Fore.RED + Style.DIM + f'{x} - {Store[Isle][x][0]} ' + Back.RESET)
                #Displays SubIsles

            SubIsle = input(Fore.GREEN + "Which subisle do you want to enter? Enter 0 to exit")
            Result = ValueCheck(SubIsle, 5)

            if (Result == None or Result == 9):
                #User entered value too great or negative or letter
                Error()
                continue

            elif (not Result):
                break
                #User entered 0 and wanted to leave

            else:
                SubIsle = int(SubIsle)
                while (loop):
                    for x in Store[Isle][SubIsle].keys():
                        # Displays Items within SubIsles
                        if (x == 0):
                            continue
                        print(Back.BLACK + Fore.BLUE + Style.DIM + f'{x} - {Store[Isle][SubIsle][x][0] : <60} - ${Store[Isle][SubIsle][x][2] : ^1} - Stock: {Store[Isle][SubIsle][x][1]}' + Back.RESET)
                    SubItem = input(Fore.GREEN + "Which item do you want? Enter 0 to exit")
                    Result = ValueCheck(SubItem, 5)

                    if (Result == None or Result == 9):
                        # User entered value too great or negative or letter
                        Error()
                        continue

                    elif(Result == 0):
                        #User wants to leave
                        break

                    else:
                        SubItem = int(SubItem)
                        while (loop):
                            print(Back.BLACK + Fore.BLUE + Style.DIM + f'{x} - {Store[Isle][SubIsle][SubItem][0] : <60} - ${Store[Isle][SubIsle][SubItem][2] : ^1} - Stock: {Store[Isle][SubIsle][SubItem][1]}' + Back.RESET)
                            #Displays selected item
                            amount = input(Fore.LIGHTGREEN_EX + Style.BRIGHT + "How many do you want? Enter 0 to exit")
                            Result = ValueCheck(amount, Store[Isle][SubIsle][SubItem][1])
                            if (Result == None):
                                Error()
                                continue
                                #Entered a negative number or letter

                            elif (Result == 9):
                                print(Fore.RED + Style.BRIGHT + "Not Enough in Stock\n")
                                continue
                                #User tried to be greedy

                            elif(Result == 0):
                                #User wants to exit
                                break

                            else:
                                amount = int(amount)
                                Store[Isle][SubIsle][SubItem][1] -= amount
                                Cart.append([Store[Isle][SubIsle][SubItem], amount, (Isle, SubIsle, SubItem)])

                                while (loop):
                                    leave = input(Fore.GREEN + "Do you want another item here? Enter Yes or No").upper()
                                    if(not(isinstance(leave, str))):
                                        Error()
                                        continue

                                    Result = ValueCheck(leave, None)
                                    if(Result == -9 or Result == None):
                                        Error()
                                        continue

                                    loop = False

                    if(Result):
                        loop = True

            if(not(Result)):
                while(True):
                    leave2 = input(Fore.GREEN + Style.DIM + "Do you want to go back to subisles, the main isles, or quit? S for SubIsles, M for Main Isles, Q for Quit: ")
                    try:
                        if (isinstance(leave2[0], str) and (leave2[0] == 'S' or leave2[0] == 'M' or leave2[0] == 'Q')):
                            break

                        else:
                            Error()
                    except IndexError:
                        Error()

            if(leave2[0] == 'Q'):
                #Ends the user input check for leaving
                break

            elif(leave2[0] == 'M'):
                #Leave to the main isles recurvisely
                Isles(Store, Cart)
                break


def Processing(Cart, Store):
    for x in range(len(Cart)-1):
        y = Cart[x][0][0]
        for z in range(len(Cart) -1):
            print(y)
            print(Cart[z+1][0][0])

            if(z < x):
                continue
            elif (y == Cart[z+1][0][0]):
                Cart[x][1] += Cart[z+1][1]
                Cart.pop(z+1)
    #Add duplicate items together and removes the duplicate from the cart

    loop = True
    while (loop):
        #Item Return Loop
        print(Fore.GREEN + Style.DIM + "--------------------------------------------------------------------------------")
        print(f'{Back.WHITE + Fore.BLACK}{"Item": ^65}-{"Qty": ^6}- {"Price": <9}{Back.RESET + Fore.RESET + Style.RESET_ALL}')
        for x in range(len(Cart)):
            print(f'{Back.WHITE + Fore.BLACK}{x + 1} - {Cart[x][0][0] : <61}-{Cart[x][1]: ^6}- {"$" + str(Cart[x][0][2]): <9}{Back.RESET + Fore.RESET + Style.RESET_ALL}')
        #Displays items in cart and their respective index

        while (loop):
            Return = input(Back.BLACK + Fore.WHITE + "Do you want to return an item? Yes or No: ").upper()
            if(not(isinstance(Return, str))):
                Error()
                continue

            Result1 = ValueCheck(Return, None)
            if(Result1 == -9 or Result1 == None):
                Error()
                continue
            elif(Result1 and len(Cart) == 0):
                print(Fore.RED + Style.BRIGHT + "You have no items in your cart" + Back.RESET)
                Result1 = False
                break

            else:
                break


        if(Result1):
            while (loop):
                index = input(Back.BLACK + Fore.WHITE + "Which item do you want to remove? Enter 0 to quit: ")
                Result2 = ValueCheck(index, len(Cart))

                if (Result2 == None):
                    Error()
                    continue
                    # Entered a negative number or letter

                elif (Result2 == 9):
                    print(f'{Fore.RED + Style.BRIGHT}You do not have {index} items in your cart\n')
                    continue
                    # User thought they had more than what's in the cart

                elif (Result2 == 0):
                    # User wants to exit
                    break

                else:

                    index = int(index) - 1
                    if (len(Cart[index][2]) == 2):
                        while(loop):
                            ReturnAmount = input(Back.BLACK + Fore.WHITE + "Do you want to return everything? Yes or No: ")
                            if (not(isinstance(ReturnAmount, str))):
                                Error()
                                continue

                            Result3 = ValueCheck(ReturnAmount, None)
                            if (Result3 == -9 or Result3 == None):
                                Error()
                                continue

                            else:
                                break

                        if (not(Result3)):
                            while(loop):
                                Qty = input(Back.BLACK + Fore.WHITE + "How many do you want to return? Enter 0 to Quit:  ")
                                Result4 = ValueCheck(Qty, Cart[index][1])
                                Qty = int(Qty)

                                if (Result4 == None):
                                    Error()
                                    continue
                                    #Entered a negative number or letter

                                elif (Result4 == 9):
                                    print(Fore.RED + Style.BRIGHT + "Greater than what you have in your cart\n")
                                    continue
                                    #User tried to be unreasonable

                                elif(Result4 == 0):
                                    #User wants to exit
                                    break

                                else:
                                    Store[Cart[index][2][0]][Cart[index][2][1]][1] += Qty
                                    Cart[index][1] -= Qty
                                    if(not(Cart[index][1])):
                                        Cart.pop(index)
                                    break

                        else:

                            Store[Cart[index][2][0]][Cart[index][2][1]][1] += Cart[index][1]
                            Cart.pop(index)
                            break

                        if (Result4 == 0 or Result4):
                            break

                    elif (len(Cart[index][2]) == 3):
                        Store[Cart[index][2][0]][Cart[index][2][1]][Cart[index][2][2]][1] += Cart[index][1]
                        Cart.pop(index)
                        break

                if (Result2 == 0):
                    break
        else:
            while (loop):
                ReturnToShop = input(f'{Fore.LIGHTMAGENTA_EX + Back.RESET}Do you want to return to shopping? Yes or No: {Fore.RESET}')
                if (not (isinstance(ReturnToShop, str))):
                    Error()
                    continue

                Result5 = ValueCheck(ReturnToShop, None)
                if (Result5 == -9 or Result5 == None):
                    Error()
                    continue

                elif (Result5):
                    Isles(Store, Cart)
                    break

                elif (not (Result5)):
                    break
                    # User Wants to leave

            if(not(Result5)):
                PrintRecipt(Cart)
                break


def PrintRecipt(Cart):
    subtotal = 0
    tax = 0.065
    filler = ' ' * 28
    style = Back.WHITE + Fore.BLACK
    Reset = Back.RESET + Fore.RESET + Style.RESET_ALL

    print(" ")
    print(f'{Back.BLACK + Fore.RED}{"Shoppers World": ^79}{Back.RESET}')
    print(f'{style}{"-" * 79}{Reset}')
    print(f'{style}{"Item": ^61}-{"Qty": ^6}- {"Price": <9}{Reset}')
    for x in range(len(Cart)):
        print(f'{style}{Cart[x][0][0] : <61}-{Cart[x][1]: ^6}- {"$" + str(Cart[x][0][2]): <9}{Reset}')
        subtotal += Cart[x][1] * Cart[x][0][2]
    # Displays items in cart
    print(f'{style}{"-" * 79}{Reset}')

    total = subtotal + (subtotal * tax)
    print(f'{style}{" "* 79}{Reset}\n'
          f'{style}{"Subtotal": >30} {subtotal: >20}{filler}{Reset}\n'
          f'{style}{"---------": >51}{" " * 28}{Reset}\n'
          f'{style}{"Tax": >30} {tax: >20}{filler}{Reset}\n'
          f'{style}{"---------": >51}{" " * 28}{Reset}\n'
          f'{style}{"Total": >30} {total: >20}{filler}{Reset}\n'
          f'{style}{" " * 79}{Reset}\n'
          f'{style}{"Visa ************1932": >30} {total: >20}{filler}{Reset}\n'
          f'{style}{"--------": >51}{" " * 28}{Reset}\n'
          f'{style}{"Amount Paid": >30} {total: >20}{filler}{Reset}\n'
          f'{style}{" "* 79}{Reset}'

          )

def ItemSearch(Store):
    loop = True
    style = Back.WHITE + Fore.BLACK
    Reset = Back.RESET + Fore.RESET + Style.RESET_ALL

    while(loop):
        ask = input(Fore.LIGHTCYAN_EX + "Do you want to search the store for an item? Y/N: ")
        if(not(isinstance(ask, str))):
            Error()
            continue

        Result = ValueCheck(ask, None)
        if(Result == -9):
            Error()
            continue

        elif(Result):
             PotentialItems = []
             Item = input("Enter the item name: ")

             print(f'{style}{"-" * 88}{Reset}')
             print(f'{style}{"Item": ^61}-{"Isle": ^6}-{"SubIsle": ^9}-{"Number": ^9}{Reset}')

             for a in range(len(Item)):

                Sfilter = str(Item)[0: len(Item) - a]
                if(len(Item) != 1 and len(Sfilter) == 1):
                    break

                for x in range(len(Store.keys())):
                     if(x == 0):
                         continue
                     for y in range(len(Store[x].keys())):
                         if(y == 0):
                             continue

                         if(x < 6):
                             item = Store[x][y][0]
                             Words = Store[x][y][0].split()

                             for b in Words:
                                 if(Sfilter == b[0:len(Sfilter)] and item not in PotentialItems):
                                     PotentialItems.append(item)
                                     print(f'{style}{item: <61}-{x:^6}-{"None":^9}-{y:^9}{Reset}')

                         if (x >= 7):
                             for z in range(len(Store[x][y].keys())):
                                 if(z == 0):
                                    continue
                                 item = Store[x][y][z][0]
                                 Words = Store[x][y][z][0].split()

                                 for b in Words:
                                     if (Sfilter == b[0:len(Sfilter)] and item not in PotentialItems):
                                         PotentialItems.append(item)
                                         print(f'{style}{item: <61}-{x:^6}-{y:^9}-{z:^9}{Reset}')



        elif(Result == -9):
            Error()
            continue

        else:
            break



def Error():
    print(Fore.RED + Style.BRIGHT + "Error! The value you entered was not a valid response!\n")


def ValueCheck(Value, limit):
    Value = Value.upper()

    if(limit == None):
        try:
            if (Value[0] == 'N' or Value[0] == 'Q'):
                return False

            elif (Value[0] == 'Y' or Value[0] == 'M'):
                return True

            else:
                return -9

        except IndexError:
            return None

    elif(not(limit == None)):
        try:
            Value = int(Value)

        except ValueError:
            return None

        else:
            if (Value < 0):
                return None

            elif(Value > limit):
                return 9

            elif(Value == 0):
                return 0

            else:
                return True
    else:
        Error()


def main():
    loop = True

    while(loop):
        shop = input(Fore.LIGHTMAGENTA_EX + "Do you want to shop here? Yes or No: ").upper()

        try:
            if(shop[0] == 'Y'):
                ShopperWRLD()
                break
            elif(shop[0] == 'N'):
                break
        except IndexError:
            Error()

    print(" ")
    print(Fore.YELLOW + Back.BLACK + "Have a blessed day!" + Back.RESET)

main()
