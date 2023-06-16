import math
import datetime

width = int(input("Enter the width pf the tire in mm (ex 205) : "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60) :"))
diametar_of_wheel = int(input("Enter the diameter of the wheel in inches (ex 15) :" ))
print()
                   # Volume formula
vol_formula = math.pi * width**2 * ratio*(width * ratio + 2540 * diametar_of_wheel) / 10000000000

print (f"The aproximate volume is ${vol_formula:.2f} liters.")
print()
#Asking the user if she wants to buy tires with the dimensions that she entered. and If the user answers “yes”, The program  ask for her phone number and store her phone number in the volumes.txt file.

continu = input("Do you want to buy tires with the dimensions that you entered? (yes/no)  ")
number = " "
if continu == "no":
    print("Thanks to join us bye!")
elif continu == "yes":
    number = input("Type your phone number here:  ")    
else :
    print("[Erro]")

#appending to the end of the volumes.txt file one line that contains the following values:, current date, width of the tire. aspect ratio of the tire, diameter of the wheel, volume of the tire

date_time = datetime.datetime.now()
volume = open("volume.txt","a")
volume.write(f"{date_time: %Y-%m-%d} , {width} , {ratio} , {diametar_of_wheel} , {vol_formula:.2f} \n" )
print()
volume.write(number)
volume.close()
