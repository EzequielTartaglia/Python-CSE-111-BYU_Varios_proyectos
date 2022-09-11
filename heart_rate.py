"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.

"""

print('')
print("Welcome to the Cardiac Strength Simulator")
print('')
use_simulator = input('Would you like to use the Cardiac Strength Simulator? ').lower()
print('')
while use_simulator != 'no':
    if (use_simulator == 'yes'):

        person_age = int(input("Could you write your age, please?"))
        print('')

        #Formula
        max_rate = 220 - person_age
        faster_frequence = max_rate*0.85 #max frequence of heart beat
        slower_frequence = max_rate*0.65 #min frequence of heart beat

        #Result
        print("When exercising to strengthen your heart")
        print(f"you should keep your heart rate, during 20 minutes, between {slower_frequence:.0f} and {faster_frequence:.0f} of your heart's maximum rate")
        use_simulator = 'no' #to finish the loop
    
    elif (use_simulator == 'no'):
        print("Might in other ocation, good bye.")

print('')
print('')