#################################################################### Instructions ##########################################################################

#A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
# Write a Python program named boxes.py that asks the user for two integers:

#the number of manufactured items
#the number of items that the user will pack per box

#Your program must compute and print the number of boxes necessary to hold the items. 
#This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.

###########################################################################################################################################################

#import math methods
import math

#Inputs (get the values)
print()
number_of_items = int(input("Enter the number of items: ")) #Total number of items
box_size_package = int(input("Enter the number of items per box: ")) #Max items per box

#Formula
total_boxes = math.ceil(number_of_items / box_size_package) #math.ceil(x) round to the next number (because in this case
                                                                  #you need another box if the items not is exacly, no less)

#Final print
print()
print(f"For {number_of_items} items, packing {box_size_package} items in each box, you will need {total_boxes} boxes.")