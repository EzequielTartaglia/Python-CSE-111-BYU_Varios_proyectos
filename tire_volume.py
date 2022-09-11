
#Import library of math formulas (pi, for example)
import math 

print('')
print("Welcome to the car tire size simulator (United States)")
print('')
print('This program computes and outputs the')
print('The volume of space inside a tire')
print('')

#Get information from inputs to the user (calculate the volume of the tire)
width_tire = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio_tire = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_wheel = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#Formula
volume_in_liters = (math.pi*(width_tire**2)*aspect_ratio_tire*(width_tire*aspect_ratio_tire + 2540*diameter_wheel)) /10000000000

print('')
print(f"The approximate volume is {volume_in_liters:.2f} liters")