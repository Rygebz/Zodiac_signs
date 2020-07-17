import os
from datetime import date
import time
import sys

print("Signs of the zodiac\n \
Welcome! \
Are u want to know what is your Zodiac sign? \
You have your choice!")

while True:
	choice = int(input("Write your choice! (Choice is in [1] - Yes, [2] - No):\n "))

	if choice in (1, 2):
		if choice == 1:
			print("U took a good choice\n")
		elif choice == 2:
			print("Meh, why U don't want to know :(")
			
		break
	
if choice == 1:
	print("Ok, you took GOOD choice you know what now?\n")
if choice == 2:
	sys.exit()

Month = int(input("Enter the number of the month in which you were born: "))
print("Ok, U done that good. \
Then. Now!\n")
Day = int(input("Enter the number of the day in which you were born: "))
print("Wait a second")
time.sleep(2)
print("Here Ur zodiac sign:")
if ((int(Month) == 1 and int(Day) >= 20) or (int(Month) == 2 and int(Day) <= 18)):
	print("Aquarius") 
elif ((int(Month) == 2 and int(Day) >= 19) or (int(Month) == 3 and int(Day) <= 20)):
	print("Pisces")
elif ((int(Month) == 3 and int(Day) >= 21) or (int(Month) == 4 and int(Day) <= 19)):
	print("Aries")
elif ((int(Month) == 4 and int(Day) >= 20) or (int(Month) == 5 and int(Day) <= 20)):
	print("Taurus")
elif ((int(Month) == 5 and int(Day) >= 21) or (int(Month) == 6 and int(Day) <= 20)):
	print("Gemini")
elif ((int(Month) == 6 and int(Day) >= 21) or (int(Month) == 7 and int(Day) <= 22)):
	print("Cancer") 
elif ((int(Month) == 7 and int(Day) >= 23) or (int(Month) == 8 and int(Day) <= 22)):
	print("Leo")
elif ((int(Month) == 8 and int(Day) >= 23) or (int(Month) == 9 and int(Day) <= 22)):
	print("Virgo")
elif ((int(Month) == 9 and int(Day) >= 23) or (int(Month) == 10 and int(Day) <= 22)):
	print("Libra")
elif ((int(Month) == 10 and int(Day) >= 23) or (int(Month) == 11 and int(Day) <= 21)):
	print("Scorpio")
elif ((int(Month) == 11 and int(Day) >= 22) or (int(Month) == 12 and int(Day) <= 21)):
	print("Sagittarius") 
elif ((int(Month) == 12 and int(Day) >= 22) or (int(Month) == 1 and int(Day) <= 19)):
	print("Capricorn") 
