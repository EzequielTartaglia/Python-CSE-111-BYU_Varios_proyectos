
################################################################ Date & time (currenly) ############################################################################### 

#Get the date and time of our computer system
from datetime import datetime
import os

UNDERLINE = '\033[4m'
END = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m' 
CYAN = '\033[36m'

#Get the exacly time and date
current_date_and_time = datetime.now()
print('')
print(f"{current_date_and_time:%Y-%m-%d}") #Print the time and date

############################################################################################################################################################ 



#Import library of math formulas (pi, for example)
import math 

# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volumes_tire:

    print('')
    print("Welcome to the car tire size simulator. (United States)")
    print('')
    print('This program computes and outputs the')
    print('The volume of space inside a tire.')
    print('')

    first_name_user = input("Enter your first name: "+CYAN)
    last_name_user = input(END+"Enter your last name: "+CYAN)
    cellphone_user = int(input(END+"Enter your cellphone: "+CYAN))
    print(END)
    os.system('cls')
    print(f"________________________________________________________________________________________________________________________________________________", file=volumes_tire)
    print(f" ", file=volumes_tire)
    print(f"User name: {first_name_user} {last_name_user}", file=volumes_tire) #Print the time and date
    print(f"Contact: {cellphone_user}", file=volumes_tire)
    print(f" ", file=volumes_tire)
    add_another_value = 1
    total_cart = 0 
    while add_another_value != 2:

        if add_another_value == 1:
            os.system('cls')
            #Get information from inputs to the user (calculate the volume of the tire)
            width_tire = int(input("Enter the width of the tire in mm (ex 205): "+CYAN))
            aspect_ratio_tire = int(input(END+"Enter the aspect ratio of the tire (ex 60): "+CYAN))
            diameter_wheel = int(input(END+"Enter the diameter of the wheel in inches (ex 15): "+CYAN))

            #Formula
            volume_in_liters = (math.pi*(width_tire**2)*aspect_ratio_tire*(width_tire*aspect_ratio_tire + 2540*diameter_wheel)) /10000000000

            print(END+'')
            print(f"The approximate volume is {CYAN}{volume_in_liters:.2f} liters{END}")

            #Value of the tire's package (depends of the volume_in_liters)
            if volume_in_liters <= 20:

                print('')
                print(f'The complete pack of 4 wheels and the auxiliary wheel for {CYAN}{volume_in_liters:.2f} liters{END} has a cost of {CYAN}$ 200.00{END}')
                print('')
                add_to_cart = int(input(CYAN+"Would you like to add to cart? \n\n[1] Yes \n[2] No \n\n"+END+" Your choose: "+CYAN))
                print(END)
                while add_to_cart != 2:
                    if add_to_cart == 1:
                        add_to_cart_value = 200
                        total_cart = total_cart +  add_to_cart_value
                        print('')
                        print(GREEN+'Item added successfully'+END)
                        add_to_cart = 2

                    elif add_to_cart != 1 and add_to_cart != 2:
                        print('')
                        print("Wrong. Please, choose another answer")
                        print('')
                        add_to_cart = int(input(+CYAN+"Would you like to add to cart? \n\n[1] Yes \n[2] No \n\n"+END+" Your choose: "+CYAN))
                        print(END)

            elif volume_in_liters > 20 and volume_in_liters <= 35:

                print('')
                print(f'The complete pack of 4 wheels and the auxiliary wheel for {CYAN}{volume_in_liters:.2f} liters{END} has a cost of {CYAN}$ 350.00{END}')
                print('')
                add_to_cart = int(input(CYAN+"Would you like to add to cart? \n\n[1] Yes \n[2] No \n\n"+END+" Your choose: "+CYAN))
                print(END)
                while add_to_cart != 2:
                    if add_to_cart == 1:
                        add_to_cart_value = 350
                        total_cart = total_cart +  add_to_cart_value
                        print('')
                        print(GREEN+'Item added successfully'+END)
                        add_to_cart = 2

                    elif add_to_cart != 1 and add_to_cart != 2:
                        print('')
                        print("Wrong. Please, choose another answer")
                        print('')
                        add_to_cart = int(input(CYAN+"Would you like to add to cart? \n\n[1] Yes \n[2] No \n\n"+END+" Your choose: "+CYAN))
                        print(END)

                
            elif volume_in_liters > 35:

                print('')
                print(f'The complete pack of 4 wheels and the auxiliary wheel for {CYAN}{volume_in_liters:.2f} liters{END} has a cost of {CYAN}$ 500.00{END}')
                print('')
                add_to_cart = int(input(CYAN+"Would you like to add to cart? \n\n[1] Yes \n[2] No \n\n"+END+" Your choose: "+CYAN))
                print(END)
                while add_to_cart != 2:
                    if add_to_cart == 1:
                        add_to_cart_value = 500
                        total_cart = total_cart +  add_to_cart_value
                        print('')
                        print(GREEN+'Item added successfully'+END)
                        add_to_cart = 2

                    elif add_to_cart != 1 and add_to_cart != 2:
                        print('')
                        print("Wrong. Please, choose another answer")
                        print('')
                        add_to_cart = int(input(CYAN+"Would you like to add to cart? \n\n[1] Yes \n[2] No \n\n"+END+" Your choose: "+CYAN))
                        print(END)

            print('')



########################################################## Save information in a data base (db) ############################################################ 

            # Print a volume's name and information to the file.
            print(f"Current date: {current_date_and_time:%Y-%m-%d} | Width of the tire: {width_tire} | Aspect ratio of the tire: {aspect_ratio_tire} | Diameter of the wheel: {diameter_wheel} | Volume of the tire: {volume_in_liters:.2f} [Price: $ {add_to_cart_value}]" , file=volumes_tire) #Print the time and date
            os.system('cls')
            print(f"Full purchase: {CYAN}$ {total_cart}{END}")
            print('')
            add_another_value = int(input(f"{CYAN}Would you like to add other data values? \n\n Select [1] to add data \n Select [2] to exit {END}\n\n Your choose: "+CYAN))
            print(END)
       
        elif add_another_value != 1 and add_another_value != 2:
            
            print('')
            print("Wrong. Please, choose another answer")
            print('')
            print(f"Full purchase: {CYAN} $ {total_cart}{END}")
            print('')
            add_another_value = int(input(f"{CYAN}Would you like to add other data values? \n\n Select [1] to add data \n Select [2] to exit {END}\n\n Your choose: "+CYAN))
            print(END)
    
    print(f" ", file=volumes_tire)
    print(f"Full purchase: $ {total_cart}", file=volumes_tire)
    print(f" ", file=volumes_tire)
    print(f"________________________________________________________________________________________________________________________________________________", file=volumes_tire)

####################################################################### Back-end ########################################################################### 

    #Closing program
    os.system('cls')
    print('')
    print(f"Full purchase: {CYAN}$ {total_cart}{END}")
    print('')
    print(f"Thanks for use our system {CYAN}{first_name_user}{END}. Have a nice day.")
    print('')
    print(f"{CYAN}{current_date_and_time:%Y-%m-%d}{END}") #Print the time and date
