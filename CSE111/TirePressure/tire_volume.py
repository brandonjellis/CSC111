import math
from datetime import datetime

def tire_volume(width,aspect,diameter):
    v = (math.pi*(width**2)*aspect*((width*aspect)+(2540*diameter)))/1e7
    return v

name = input("Welcome to Universal Tire Emporium!\n To begin please enter the customer's name and phone number.\nNAME: ")
phone_raw = input("PHONE NUMBER: ")
phone = ""
for i in phone_raw:
    if i.isdigit() == True:
        phone += i

print("Here are the available tire grades:")
print("BASIC\nSUPER\nSPORT\nALLWEATHER\nOFFROAD")
grade = input("Please select a tire grade.\nGRADE:").lower()

print("Tire price is determined by tire dimensions...")
start = input("Enter the tire's width in mm or enter the US standard tire code (###/###R###).\n>")
if "/" in start:
    start = start.split("/")
    start[1] = start[1].split("R")
    w = float(start[0])
    a = float(start[1][0])
    d = float(start[1][1])

else:
    w = float(start)
    a = float(input("what is the tire aspect ratio?\n>"))
    d = float(input("What is the tire diameter in inches?\n>"))



volume = tire_volume(w,a,d)
price = volume * 0.002 
if grade == "basic":
    price = price + 35
elif grade == "super":
    price = price + 50
elif grade == "sport":
    price = price * 1.10 + 75
elif grade == "allweather":
    price = price * 1.40 + 35
elif grade == "offroad":
    price = price * 2 + 35


time = str(datetime.today())
time = time.split()[0]

print("\n\nHere is your receipt:")
print(f"UNIVERSAL TIRE EMPORIUM\nDATE: {time}\nNAME: {name}\nPHONE NUMBER: {phone}\nTIRE GRADE: {grade.upper()}    VOLUME: {volume/1000:.3f}L\nUNIT PRICE: ${price:.2f}\nFULL SET PRICE: ${price*4:.2f}")


with open("tireRecord.txt", "a") as record:
    record.write(f"{time},{w},{a},{d},{volume:.3f},{name},{phone},{grade},{price:.2f},{price*4:.2f}")

