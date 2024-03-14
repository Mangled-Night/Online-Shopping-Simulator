import random
import colorama
from colorama import Fore, Back, Style
colorama.init()


def main():

#Variables 
    a = 0
    u = 0
    y = 0
    b = 0
    q = 0
    v = 0
    z = 0
    
    while ( u == 0 ):   
#Item Quantity Generator

        r = round(random.random(), 2)
        if (z == 0):
            stock = [ ]
            for n in range(84):
                R = round(100 * r)
                r = round(random.random(), 2)
                stock.append(R)
            z += 1
            cart = [ ]
            price = [ ]

#Item: Stock
        item = {
        'SAMSUNG 50" Class 4K Crystal UHD TV': stock[0],
        'EVOO 15.6" 2T Gaming Laptop': stock[1],
        "Black 32GB Samsung Galaxy A21": stock[2],
        "HP DeskJet 3772 Wireless Color Inkjet Printer": stock[3],
        "SAMSUNG Galaxy Buds+": stock[4],
        "Gucci Belt": stock[5],
        "Supreme T-Shirt": stock[6],
        "Louis Vuitton Regular Denim Jeans": stock[7],
        "41 mm Hermes Arceau Chronographe Watch": stock[8],
        "Hermes Collier de Chien Bracelet": stock[9],
        "LEGO Harry Potter Hogwarts Great Hall Set": stock[10],
        "LOL Surprise Tweens Fashion Doll Freshest": stock[11],
        "Super Smash Bros Ultimate": stock[12],
        "Beat Saber": stock[13],
        "Halo Infinite": stock[14],
        "Umbro Soccer Ball": stock[15],
        'Spalding NBA Pro Tack 28.5" Basketball' : stock[16],
        "Wilson NFL Super Grip Football ": stock[17],
        "5-25Lb Rubber Coated Hex Dumbbell Set": stock[18],
        "Abcnature 330lbs Weight Lifting Bench Multi Station": stock[19],
        "SHANY Carry All Trunk Makeup Set": stock[20],
        "Tylenol Cold + Flu Medicine Pack": stock[21],
        "Equate Antibacterial Assorted Bandages Variety Pack": stock[22],
        "Equate 70% Isopropyl Alcohol Antiseptic": stock[23],
        "Equate 91% Isopropyl Alcohol Antiseptic": stock[24],
        "JOIVI Patio Furniture Set": stock[25],
        "Walnew Adjustable Armless Swivel Bar Stool": stock[26],
        "Full Bed Frame with Wooden Headboard and Bed Frame": stock[27],
        "Queen Bed with Metal Frame": stock[28],
        "King Bed with Bed Frame and Adjustable Headboard": stock[29],
        "FurHaven Small Dog Bed": stock[30],
        "FurHaven Medium Dog Bed": stock[31],
        "FurHaven Jumbo Dog Bed": stock[32],
        "Adjustable Dog Collar and Leash Set": stock[33],
        "Purina Beggin' Strips Dog Treats": stock[34],
        "Petmaker Igloo Pet Cat Bed": stock[35],
        "Deluxe Cat Scratching Post": stock[36],
        "Pet Comb Self Cleaning Brush": stock[37],
        "Purina Tidy Cats Clumping Cat Litter": stock[38],
        "Meow Mix Dry Cat Food": stock[39],
        'REPTI-ZOO Reptile Glass Terrarium, 20" x 12" x 10': stock[40],
        "50W Reptile Heat Lamp": stock[41],
        "Reptile Terraium Decor Set": stock[42],
        "Koyal Wholesale 3 Pc DIY Terrarium Filler Kit": stock[43],
        "Frozen Large Mouse, 10 Ct": stock[44],
        "Prevue Pet Products Small Hamster Haven": stock[45],
        "Higgins Sunburst Hamster Animal Food": stock[46],
        "Gargrow Super-Silent Hamster Exercise Wheels": stock[47],
        "AKDSteel Hamster Exercise Ball": stock[48],
        "SPRING PARK DIY Hamster Tubes": stock[49],
        "AquaCulture 10 Gallon Aquarium": stock[50],
        "AquaCulture Aquarium Gravel, Rainbow, 2 lb.": stock[51],
        "AquaCulture Aquarium Gravel, AquaBlue, 2 lb.": stock[52],
        "Tetra TetraMin Tropical Flakes Fish Food, 1 oz.": stock[53],
        "GreenJoy 12 Pack Aquarium Fish Tank Decorations": stock[54],
        "Premium Breakfast Sausage Patties, 8 count": stock[55],
















        }

    #Browing Items
        print(Fore.RED + Style.DIM + "                    Welcome to Shopping WRLD")
        print("Please select the number that corralates to the item that you want to buy, then select the quantity\n\n\n")
        print("1 - Electronics and Technology")
        print("2 - Clothing, Shoes, and Accessories")
        print("3 - Toys and Games")
        print("4 - Sports and Fitness")
        print("5 - Beauty and Pharmaceutics")
        print("6 - Furniture")
        print("7 - Pets")
            #Dogs
            #Cats
            #Snakes
            #Lizards
            #Fish
        print("8 - Food")
            #Breakfast
            #Lunch
            #Dinner
            #Desert
            #Snacks

        print(Fore.RESET + Back.RESET)

    # Customer Selection
    
        while(y == 0):
            x = int(input(Fore.CYAN + "\nPlease read the instructions and select a number") )
            if (x == 1):
                y = y + 1
                while ( q == 0 ):
                    print(Fore.YELLOW + '\n1 - SAMSUNG 50" Class 4K Crystal UHD TV - $397 - ' + Back.BLACK + 'In Stock: ' + str(stock[0]) + Back.RESET)
                    print('2 - EVOO 15.6" 2T Gaming Laptop - $600 -' + Back.BLACK + 'In Stock ' + str(stock[1]) + Back.RESET)
                    print("3 - Black 32GB Samsung Galaxy A21 - $127 - "+ Back.BLACK +"In Stock: "+ str(stock[2]) + Back.RESET)
                    print("4 - HP DeskJet 3772 Wireless Color Inkjet Printer - $60 - " + Back.BLACK +"In Stock: "+ str(stock[3]) + Back.RESET)
                    print("5 - SAMSUNG Galaxy Buds+ - $100 - " + Back.BLACK +"In Stock: "+ str(stock[4]) + Back.RESET + Fore.CYAN)
                    c = int(input("\nSelect the item you want") )
                    if (c == 1 and stock[0] != 0):
                        q += 1
                        while( v == 0 ):
                            c2 = int(input("\nHow many TV's do you want?") )
                            if ( c2 > stock[0] or c2 < 0):

                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append('SAMSUNG "50" Class 4K Crystal UHD TV' )
                                price.append(c2 * 397)
                                stock[0] = stock[0] - c2

                    elif (c == 2 and stock[1] != 0):
                        q += 1
                        while( v == 0 ):
                            c2 = int(input("\nHow many laptops do you want?") )
                            if ( c2 > stock[1] or c2 < 0):

                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append('EVOO 15.6" 2T Gaming Laptop' )
                                price.append(c2 * 600)
                                stock[1] = stock[1] - c2

                    elif (c == 3 and stock[2] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many Samsung Galaxy A21s do you want?"))
                            if (c2 > stock[2] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)

                            else:
                                v += 1
                                cart.append('Black 32GB Samsung Galaxy A21')
                                price.append(c2 * 127)
                                stock[2] = stock[2] - c2

                    elif (c == 4 and stock[3] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many HP DeskJet Inkjet Printers do you want?"))
                            if (c2 > stock[3] or c2 < 0):

                                print(
                                Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append('HP DeskJet 3772  Wireless Color Inkjet Printer')
                                price.append(c2 * 60)
                                stock[3] = stock[3] - c2

                    elif (c == 5 and stock[4] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many SAMSUNG Galaxy Buds do you want?"))
                            if (c2 > stock[4] or c2 < 0):

                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append('SAMSUNG Galaxy Buds+')
                                price.append(c2 * 100)
                                stock[4] = stock[4] - c2

                    elif (c > 5):
                        print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                    else:
                        print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)


            elif(x == 2):
                y = y + 1
                while (q == 0):
                    print(Fore.YELLOW + "1 - Gucci Belt - $1,200 - " + Back.BLACK +"In Stock: "+ str(stock[5]) + Back.RESET)
                    print("2 - Supreme T-Shirt - $38 - " + Back.BLACK +"In Stock: "+ str(stock[6]) + Back.RESET)
                    print("3 - Louis Vuitton Regular Denim Jeans - $645 - " + Back.BLACK +"In Stock: "+ str(stock[7]) + Back.RESET)
                    print("4 - 41 mm Hermes Arceau Chronographe Watch - $5,250 - " + Back.BLACK +"In Stock: "+ str(stock[8]) + Back.RESET)
                    print("5 - Hermes Collier de Chien Bracelet - $49,000- " + Back.BLACK +"In Stock: "+ str(stock[9]) + Back.RESET + Fore.CYAN)
                    c = int(input("\nSelect the item you want") )
                    if (c == 1 and stock[5] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many Gucci Belts do you want?"))
                            if (c2 > stock[5] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)

                            else:
                                v += 1
                                cart.append('Gucci Belt')
                                price.append(c2 * 1200)
                                stock[5] = stock[5] - c2

                    elif (c == 2 and stock[6] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many Supreme T-Shirts do you want?"))
                            if (c2 > stock[6] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("Supreme T-Shirt")
                                price.append(c2 * 38)
                                stock[6] = stock[6] - c2

                    elif (c == 3 and stock[7] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many Louis Vuitton Jeans do you want?"))
                            if (c2 > stock[7] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("Louis Vuitton Regular Denim Jeans")
                                price.append(c2 * 645)
                                stock[7] = stock[7] - c2

                    elif (c == 4 and stock[8] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many Hermes Arceau Chronographe Watches do you want?"))
                            if (c2 > stock[8] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("41 mm Hermes Arceau Chronographe Watch")
                                price.append(c2 * 5250)
                                stock[8] = stock[8] - c2

                    elif (c == 5 and stock[9] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many Hermes Collier de Chien bracelet do you want?") )
                            if ((c2) > stock[9] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("Hermes Collier de Chien bracelet")
                                price.append(c2 * 49000)
                                stock[9] = stock[9] - c2

                    elif (c > 5):
                        print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                    else:
                        print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)



            elif(x == 3):
                y = y + 1
                while(q == 0):
                    print(Fore.YELLOW + "1 - LEGO Harry Potter Hogwarts Great Hall Set - $89 - " + Back.BLACK +"In Stock: "+ str(stock[10]) + Back.RESET)
                    print("2 - LOL Surprise Tweens Fashion Doll Freshest - $20 - " + Back.BLACK +"In Stock: "+ str(stock[11]) + Back.RESET)
                    print("3 - Super Smash Bros Ultimate - $58 - " + Back.BLACK +"In Stock: "+ str(stock[12]) + Back.RESET)
                    print("4 - Beat Saber - $30 - " + Back.BLACK +"In Stock: "+ str(stock[13]) + Back.RESET)
                    print("5 - Halo Infinite - $60 - " + Back.BLACK +"In Stock: "+ str(stock[14]) + Back.RESET + Fore.CYAN)
                    c = int(input("\nSelect the item you want") )
                    if (c == 1 and stock[10] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many LEGO Harry Potter Hogwarts Great Hall Sets do you want?"))
                            if (c2 > stock[10] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("LEGO Harry Potter Hogwarts Great Hall Set")
                                price.append(c2 * 89)
                                stock[10] = stock[10] - c2

                    elif (c == 2 and stock[11] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many LOL Surprise Tweens Fashion Doll Freshests do you want?"))
                            if (c2 > stock[11] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("LOL Surprise Tweens Fashion Doll Freshest")
                                price.append(c2 * 20)
                                stock[11] = stock[11] - c2

                    elif (c == 3 and stock[12] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many copies of Super Smash Bros Ultimate do you want?"))
                            if (c2 > stock[12] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("Super Smash Bros Ultimate")
                                price.append(c2 * 58)
                                stock[12] = stock[12] - c2

                    elif (c == 4 and stock[13] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many copies of Beat Saber do you want?"))
                            if (c2 > stock[13] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("Beat Saber")
                                price.append(c2 * 30)
                                stock[13] = stock[13] - c2

                    elif (c == 5 and stock[14] != 0):
                        q += 1
                        while (v == 0):
                            c2 = int(input("\nHow many copies of Halo Infinite do you want?"))
                            if (c2 > stock[14] or c2 < 0):
                                print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                            else:
                                v += 1
                                cart.append("Halo Infinite")
                                price.append(c2 * 60)
                                stock[14] = stock[14] - c2
                    elif (c > 5):
                        print("The number you selected is not a number listed, please select a number from the list given")

                    else:
                        print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

            elif(x == 4):
                y = y + 1
                print(Fore.YELLOW + "1 - Umbro NFHS Meteor Soccer Ball - $39 - " + Back.BLACK +"In Stock: "+ str(stock[15]) + Back.RESET)
                print('2 - Spalding NBA Pro Tack 28.5" Basketball - $18.46 - ' + Back.BLACK +"In Stock: "+ str(stock[16]) + Back.RESET)
                print("3 - Wilson NFL Super Grip Football - $26 - " + Back.BLACK +"In Stock: "+ str(stock[17]) + Back.RESET)
                print("4 - 5-25Lb Rubber Coated Hex Dumbbell Set - $360 - " + Back.BLACK +"In Stock: "+ str(stock[18]) + Back.RESET)
                print("5 - Abcnature 330lbs Weight Lifting Bench Multi Station - $250 - " + Back.BLACK +"In Stock: "+ str(stock[19]) + Back.RESET + Fore.CYAN)
                c = int(input("\nSelect the item you want"))
                if (c == 1 and stock[15] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Umbro Soccer Balls do you want?"))
                        if (c2 > stock[15] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                        else:
                            v += 1
                            cart.append("Umbro Soccer Ball")
                            price.append(c2 * 39)
                            stock[15] = stock[15] - c2

                elif (c == 2 and stock[16] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Spalding Basketballs do you want?"))
                        if (c2 > stock[16] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                        else:
                            v += 1
                            cart.append('Spalding NBA Pro Tack 28.5" Basketball')
                            price.append(c2 * 18.46)
                            stock[16] = stock[16] - c2

                elif (c == 3 and stock[17] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Wilson Footballs do you want?"))
                        if (c2 > stock[17] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                        else:
                            v += 1
                            cart.append("Wilson NFL Super Grip Football")
                            price.append(c2 * 26)
                            stock[17] = stock[17] - c2

                elif (c == 4 and stock[18] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Dumbell Sets do you want?"))
                        if (c2 > stock[18] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                        else:
                            v += 1
                            cart.append("5-25Lb Rubber Coated Hex Dumbbell Set")
                            price.append(c2 * 360)
                            stock[18] = stock[18] - c2

                elif (c == 5 and stock[19] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN))
                        if (c2 > stock[19] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN)
                        else:
                            v += 1
                            cart.append("Abcnature 330lbs Weight Lifting Bench Multi Station")
                            price.append(c2 * 250)
                            stock[19] = stock[19] - c2

                elif (c > 5):
                    print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                else:
                    print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

            elif(x == 5):
                y = y + 1
                print(Fore.YELLOW + "1 - SHANY Carry All Trunk Makeup Set - $45.49 - " + Back.BLACK + "In Stock: " + str(stock[20]) + Back.RESET)
                print("2 - Tylenol Cold + Flu Medicine Pack - $6.48 - " + Back.BLACK + "In Stock: " + str(stock[21]) + Back.RESET)
                print("3 - Equate Antibacterial Assorted Bandages Variety Pack, 120 Count - $6.67 - " + Back.BLACK + "In Stock: " + str(stock[22]) + Back.RESET)
                print("4 - Equate 70% Isopropyl Alcohol Antiseptic, 32 fl oz - $2.18 - " + Back.BLACK + "In Stock: " + str(stock[23]) + Back.RESET)
                print("5 - Equate 91% Isopropyl Alcohol Antiseptic, 32 fl oz - $2.78 - " + Back.BLACK + "In Stock: " + str(stock[24]) + Back.RESET + Fore.CYAN)
                c = int(input("\nSelect the item you want"))
                if (c == 1 and stock[20] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Makeup Sets do you want?"))
                        if (c2 > stock[20] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )
                                
                        else:
                            v += 1
                            cart.append("SHANY Carry All Trunk Makeup Set")
                            price.append(c2 * 45.49)
                            stock[20] = stock[20] - c2

                elif (c == 2 and stock[21] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Tylenol Cold + Flu Medicine packs do you want?"))
                        if(c2 > stock[21] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("Tylenol Cold + Flu Medicine Pack")
                            price.append(c2 * 6.48)
                            stock[21] -= c2

                elif (c == 3 and stock[22] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Equate Antibacterial Assorted Bandages Variety Pack do you want?"))
                        if(c2 > stock[22] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("Equate Antibacterial Assorted Bandages Variety Pack")
                            price.append(c2 * 6.67)
                            stock[22] -= c2

                elif (c == 4 and stock[23] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Equate 70% Isopropyl Alcohol bottles do you want?"))
                        if (c2 > stock[23] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("Equate 70% Isopropyl Alcohol Antiseptic")
                            price.append(c2 * 2.18)
                            stock[23] -= c2

                elif (c == 5 and stock[24] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Equate 91% Isopropyl Alcohol bottles do you want?"))
                        if (c2 > stock[24] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("Equate 91% Isopropyl Alcohol Antiseptic")
                            price.append(c2 * 2.78)
                            stock[24] -= c2

                elif (c > 5):
                    print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                else:
                    print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

                
            elif(x == 6):
                y = y + 1
                print(Fore.YELLOW + "1 - JOIVI Patio Furniture Set - $500 - " + Back.BLACK + "In Stock: " + str(stock[25]) + Back.RESET)
                print("2 - Walnew Adjustable Armless Swivel Bar Stool - $45 - " + Back.BLACK + "In Stock: " + str(stock[26]) + Back.RESET)
                print("3 - Full Bed with Wooden Headboard and Bed Frame - $180 - " + Back.BLACK + "In Stock: " + str(stock[27]) + Back.RESET)
                print("4 - Queen Bed with Metal Frame - $192 - " + Back.BLACK + "In Stock: "+ str(stock[28]) + Back.RESET)
                print("5 - King Bed with Bed Frame and Adjustable Headboard - $220 - " + Back.BLACK + "In Stock: " + str(stock[29]) + Back.RESET + Fore.CYAN)
                c = int(input("Select the item you want") )
                if (c == 1 and stock[25] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Furniture Sets do you want?"))
                        if (c2 > stock[25] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("JOVI Patio Furniture Set")
                            price.append(c2 * 500)
                            stock[25] -= c2

                elif (c == 2 and stock[26] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many Armless Swivel Bar Stools do you want?"))
                        if (c2 > stock[26] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("Walnew Adjustable Armless Swivel Bar Stool")
                            price.append(c2 * 45)
                            stock[26] -= c2

                elif (c == 3 and stock[27] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many full beds you want?"))
                        if (c2 > stock[27] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("Full Bed with Wooden Headboard and Bed Frame")
                            price.append(c2 * 45)
                            stock[27] -= c2

                elif (c == 4 and stock[28] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many queen beds do you want?"))
                        if (c2 > stock[28] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("Queen Bed with Metal Frame")
                            price.append(c2 * 192)
                            stock[28] -= c2

                elif (c == 5 and stock[29] != 0):
                    q += 1
                    while (v == 0):
                        c2 = int(input("\nHow many king beds do you want?"))
                        if (c2 > stock[29] or c2 < 0):
                            print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                        else:
                            v += 1
                            cart.append("King Bed with Bed Frame and Adjustable Headboard")
                            price.append(c2 * 220)
                            stock[29] -= c2

                elif (c > 5):
                    print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                else:
                    print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

            elif(x == 7):
                y = y + 1
                print("1 - Dogs")
                print("2 - Cats")
                print("3 - Snakes")
                print("4 - Hamsters")
                print("5 - Fish")
                while (a == 0):
                    sub1 = int(input("Please select a subsection"))
                    if (sub1 == 1):
                        a = a + 1
                        print(Fore.YELLOW + "1 - FurHaven Small Dog Bed - $21 - " + Back.BLACK + "In Stock: " + str(stock[30]) + Back.RESET)
                        print("2 - PEDIGREE Small Dog Complete Nutrition, 15.9 lbs - $11.74 - " + Back.BLACK + "In Stock: " + str(stock[31]) + Back.RESET)
                        print("3 - PEDIGREE Adult Dog Complete Nutrition, 20.4 lbs - $13.49 - " + Back.BLACK + "In Stock: " + str(stock[32]) + Back.RESET)
                        print("4 - Adjustable Dog Collar and Leash Set - $12 - " + Back.BLACK + "In Stock: " + str(stock[33]) + Back.RESET)
                        print("5 - Purina Beggin' Strips Dog Treats, 6 oz. - $2.84 - " + Back.BLACK + "In Stock: " + str(stock[34]) + Back.RESET + Fore.CYAN)
                        c = int(input("Select the item you want") )
                        if (c == 1 and stock[30] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many small dog beds do you want?"))
                                if (c2 > stock[30] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("FurHaven Small Dog Bed")
                                    price.append(c2 * 21)
                                    stock[30] -= c2

                        if (c == 2 and stock[31] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bags of small breed dog food do you want?"))
                                if (c2 > stock[31] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("PEDIGREE Small Dog Complete Nutrition")
                                    price.append(c2 * 11.74)
                                    stock[31] -= c2

                        if (c == 3 and stock[32] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bags of adult dog food do you want?"))
                                if (c2 > stock[32] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("PEDIGREE Adult Dog Complete Nutrition")
                                    price.append(c2 * 13.49)
                                    stock[32] -= c2

                        if (c == 4 and stock[33] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many dog leashes and collars do you want?"))
                                if (c2 > stock[33] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Adjustable Dog Collar and Leash Set")
                                    price.append(c2 * 12)
                                    stock[33] -= c2

                        if (c == 5 and stock[34] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bags of dogs treats do you want?"))
                                if (c2 > stock[34] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Purina Beggin' Strips Dog Treats")
                                    price.append(c2 * 2.84)
                                    stock[34] -= c2

                        elif (c > 5):
                            print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                        else:
                            print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

                    elif (sub1 == 2):
                        a = a + 1
                        print(Fore.YELLOW + "1 - Petmaker Igloo Pet Cat Bed - $16 - " + Back.BLACK + "In Stock: " + str(stock[35]) + Back.RESET)
                        print("2 - Deluxe Cat Scratching Post - $20 - " + Back.BLACK + "In Stock: " + str(stock[36]) + Back.RESET)
                        print("3 - Pet Comb Self Cleaning Brush - $13 - " + Back.BLACK + "In Stock: " + str(stock[37]) + Back.RESET)
                        print("4 - Purina Tidy Cats Clumping Cat Litter, 35 lbs - $16.48 - " + Back.BLACK + "In Stock: " + str(stock[38]) + Back.RESET)
                        print("5 - Meow Mix Dry Cat Food, 16 lbs - $12.12 - " + Back.BLACK + "In Stock: " + str(stock[39]) + Back.RESET + Fore.CYAN)
                        c = int(input("Select the item you want"))
                        if (c == 1 and stock[35] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many cat beds do you want?"))
                                if (c2 > stock[35] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Petmaker Igloo Pet Cat Bed")
                                    price.append(c2 * 16)
                                    stock[35] -= c2

                        elif (c == 2 and stock[36] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many scratching posts do you want?"))
                                if (c2 > stock[36] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Deluxe Cat Scratching Post")
                                    price.append(c2 * 20)
                                    stock[36] -= c2

                        elif (c == 3 and stock[37] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many cleaning brushes do you want?"))
                                if (c2 > stock[37] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Pet Comb Self Cleaning Brush")
                                    price.append(c2 * 13)
                                    stock[37] -= c2

                        elif (c == 4 and stock[38] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bins of cat litter do you want?"))
                                if (c2 > stock[38] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Purina Tidy Cats Clumping Cat Litter")
                                    price.append(c2 * 16.48)
                                    stock[38] -= c2

                        elif (c == 5 and stock[39] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bags of cat food do you want?"))
                                if (c2 > stock[39] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Meow Mix Dry Cat Food")
                                    price.append(c2 * 12.12)
                                    stock[38] -= c2

                        elif (c > 5):
                            print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                        else:
                            print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

                    elif (sub1 == 3):
                        a = a + 1
                        print(Fore.YELLOW + '1 - REPTI-ZOO Reptile Glass Terrarium, 20" x 12" x 10" - $80 - ' + Back.BLACK + "In Stock: " + str(stock[40]) + Back.RESET)
                        print("2 - Eccomum 50W Reptile Heat Lamp - $24 - " + Back.BLACK + "In Stock: " + str(stock[41]) + Back.RESET)
                        print("3 - Reptile Terraium Decor Set - $69 - " + Back.BLACK + "In Stock: " + str(stock[42]) + Back.RESET)
                        print("4 - Koyal Wholesale 3 Pc DIY Terrarium Filler Kit - $17 - " + Back.BLACK + "In Stock: " + str(stock[43]) + Back.RESET)
                        print("5 - Frozen Large Mouse, 10 Ct - $22 - " + Back.BLACK + "In Stock: " + str(stock[44] + Back.RESET) + Fore.CYAN)

                        int(input("Select the item you want"))
                        if (c == 1 and stock[40] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many starter kits do you want?"))
                                if (c2 > stock[40] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append('REPTI-ZOO Reptile Glass Terrarium, 20" x 12" x 10"')
                                    price.append(c2 * 80)
                                    stock[40] -= c2

                        elif (c == 2 and stock[41] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many heat lamps do you want?"))
                                if (c2 > stock[40] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("50W Reptile Heat Lamp")
                                    price.append(c2 * 24)
                                    stock[41] -= c2

                        elif (c == 3 and stock[42] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many decor kits do you want?"))
                                if (c2 > stock[42] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Reptile Terraium Decor Set")
                                    price.append(c2 * 69)
                                    stock[42] -= c2

                        elif (c == 4 and stock[43] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many filler kits do you want?"))
                                if (c2 > stock[43] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Koyal Wholesale 3 Pc DIY Terrarium Filler Kit")
                                    price.append(c2 * 17)
                                    stock[43] -= c2

                        elif (c == 5 and stock[44] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many boxes of frozen mice do you want?"))
                                if (c2 > stock[44] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Frozen Large Mouse, 10 Ct")
                                    price.append(c2 * 22)
                                    stock[44] -= c2

                        elif (c > 5):
                            print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                        else:
                            print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

                    elif (sub1 == 4):
                        a = a + 1
                        print(Fore.YELLOW + "1 - Prevue Pet Products Small Hamster Haven - $47.43 - " + Back.BLACK + "In Stock: " + str(stock[45]) + Back.RESET)
                        print("2 - Higgins Sunburst Hamster Animal Food, 2.5 Lb - $15 - " + Back.BLACK + "In Stock: " + str(stock[46]) + Back.RESET)
                        print("3 - Gargrow Super-Silent Hamster Exercise Wheels - $10.12 - " + Back.BLACK + "In Stock: " + str(stock[47]) + Back.RESET)
                        print("4 - AKDSteel Hamster Exercise Ball - $8.09 - " + Back.BLACK + "In Stock: " + str(stock[48]) + Back.RESET)
                        print("5 - SPRING PARK DIY Hamster Tubes Set - $9.13 - " + Back.BLACK + "In Stock: " + str(stock[49]) + Back.RESET + Fore.CYAN)


                        c = int(input("Select the item you want"))
                        if (c == 1 and stock[45] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many hamster cages do you want?"))
                                if (c2 > stock[45] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Prevue Pet Products Small Hamster Haven")
                                    price.append(c2 * 47.43)
                                    stock[45] -= c2

                        elif (c == 2 and stock[46] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bags of hamster food do you want?"))
                                if (c2 > stock[46] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Higgins Sunburst Hamster Animal Food")
                                    price.append(c2 * 15)
                                    stock[46] -= c2

                        elif (c == 3 and stock[47] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many hamster wheels do you want?"))
                                if (c2 > stock[47] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Gargrow Super-Silent Hamster Exercise Wheels")
                                    price.append(c2 * 10.12)
                                    stock[47] -= c2

                        elif (c == 4 and stock[48] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many hamster balls do you want?"))
                                if (c2 > stock[48] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("AKDSteel Hamster Exercise Ball")
                                    price.append(c2 * 8.09)
                                    stock[48] -= c2

                        elif (c == 5 and stock[49] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many hamster tube sets do you want?"))
                                if (c2 > stock[49] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("SPRING PARK DIY Hamster Tubes")
                                    price.append(c2 * 9.13)
                                    stock[49] -= c2

                        elif (c > 5):
                            print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                        else:
                            print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

                    elif (sub1 == 5):
                        a = a + 1
                        print(Fore.YELLOW + "1 - AquaCulture 10 Gallon Aquarium - $18.30 - " + Back.BLACK + "In Stock: " + str(stock[50]) + Back.RESET)
                        print("2 - AquaCulture Aquarium Gravel, Rainbow, 2 lb. - $3 - " + Back.BLACK + "In Stock: " + str(stock[51]) + Back.RESET)
                        print("3 - AquaCulture Aquarium Gravel, AquaBlue, 2 lb. - $2.45 - " + Back.BLACK + "In Stock: " + str(stock[52]) + Back.RESET)
                        print("4 - Tetra TetraMin Tropical Flakes Fish Food, 1 oz. - $4.23 - " + Back.BLACK + "In Stock: " + str(stock[53]) + Back.RESET)
                        print("5 - GreenJoy 12 Pack Aquarium Fish Tank Decorations - $15.88 - " + Back.BLACK + "In Stock: " + str(stock[54]) + Back.RESET + Fore.CYAN)


                        c = int(input("Select the item you want"))
                        if (c == 1 and stock[50] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many aquariums do you want?"))
                                if (c2 > stock[50] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("AquaCulture 10 Gallon Aquarium")
                                    price.append(c2 * 18.30)
                                    stock[50] -= c2

                        elif (c == 2 and stock[51] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bags of gravel do you want?"))
                                if (c2 > stock[51] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("AquaCulture Aquarium Gravel, Rainbow, 2 lb.")
                                    price.append(c2 * 3)
                                    stock[51] -= c2

                        elif (c == 3 and stock[52] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many bags of gravel do you want?"))
                                if (c2 > stock[52] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("AquaCulture Aquarium Gravel, AquaBlue, 2 lb.")
                                    price.append(c2 * 3)
                                    stock[52] -= c2

                        elif (c == 4 and stock[53] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many containers of fish food do you want?"))
                                if (c2 > stock[53] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Tetra TetraMin Tropical Flakes Fish Food, 1 oz.")
                                    price.append(c2 * 4.23)
                                    stock[53] -= c2

                        elif (c == 5 and stock[54] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many decoration packs do you want?"))
                                if (c2 > stock[54] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("GreenJoy 12 Pack Aquarium Fish Tank Decorations")
                                    price.append(c2 * 15.88)
                                    stock[54] -= c2

                        elif (c > 5):
                            print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                        else:
                            print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

                    elif (sub1 > 5):
                        print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

                    else:
                        print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)


            elif(x == 8):
                y = y + 1
                print("1 - Breakfast")
                print("2 - Lunch")
                print("3 - Dinner")
                print("4 - Desert")
                print("5 - Snacks")
                while(a == 0):
                    sub1 = int(input("Please select a subsection") )
                    if (sub1 == 1):
                        a = a + 1
                        print(Fore.YELLOW + "1 - Great Value Premium Breakfast Sausage Patties, 8 count - $2.76 - " + Back.BLACK + "In Stock: " + str(stock[55]) + Back. RESET)

                        c = int(input("Select the item you want"))
                        if (c == 1 and stock[55] != 0):
                            q += 1
                            while (v == 0):
                                c2 = int(input("\nHow many packs of sausage patties do you want?"))
                                if (c2 > stock[55] or c2 < 0):
                                    print(Fore.RED + Style.BRIGHT + "\nThe amount you entered is larger than what we have in stock please enter a lower number" + Style.RESET_ALL + Fore.CYAN )

                                else:
                                    v += 1
                                    cart.append("Premium Breakfast Sausage Patties, 8 count")
                                    price.append(c2 * 2.76)
                                    stock[55] -= c2
                    elif(sub1 == 2):
                        a = a + 1
                        print("Select the item you want")

                    elif(sub1 == 3):
                        a = a + 1
                        print("Select the item you want")

                    elif(sub1 == 4):
                        a = a + 1
                        print("Select the item you want")
                        
                    elif(sub1 == 5):
                        a = a + 1
                        print("Select the item you want")


                    elif (sub1 > 5):
                        print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)


                    else:
                        print(Fore.RED + Style.BRIGHT + "We are currently have no more of that item in stock, please try again tomorrow" + Style.RESET_ALL + Fore.CYAN)

            else:
                print(Fore.RED + Style.BRIGHT + "The number you selected is not a number listed, please select a number from the list given" + Style.RESET_ALL + Fore.CYAN)

        f = 0
        while (f == 0):
            contin = input('Do you want to continue shopping? Enter "Yes" or "No" ')
            if (contin == "No" or contin == "no" ):
                u += 1
                f += 1

            elif (contin == "Yes" or contin == "yes"):
                y = 0
                a = 0
                v = 0
                q = 0
                f += 1
            else:
                print("")
                print(Fore.WHITE + 'Please type "Yes/yes" or "No/no"' + Fore.CYAN)


        

main()
