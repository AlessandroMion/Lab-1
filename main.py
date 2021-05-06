#Question 1 
#Make different varibales for first and last name
First = str(input(" What is your first name? "))
Last = str(input(" What is your last name? "))
#This just reverses the order
print(Last,First)

#Question 2
#Create number and a represents it is a checker to see if its even odd or zero.
Number = int(input("Enter a number: "))
a = Number % 2
#This means if the number =0 it will understand it is 0
if  Number == 0:
    print("The number is 0.")
#This means if number is over a 0 it is odd because the numbers dont have different reminders if they are divided by two
elif a > 0:
    print("The number is odd.")
#This means if anything is else it is even
else: 
    print("The number is even.")

#Question 3
#Make a varibale as day and input a question meaning that I will give you the date with the number
Day = int(input("Give me a number I give you the date, "))
#Copy and paste and fix every single one to match the correct date, this is with the month and the date with the exact numbers.
if Day >= 1 and Day <= 31:
  print("January ", Day)
if Day >= 32 and Day <= 59:
  print("Feburary ", Day -31)
if Day >= 60 and Day <= 90:
  print("March ", Day -59)
if Day >= 91 and Day <= 120:
  print("April ", Day -91)
if Day >= 121 and Day <= 151:
  print("May ", Day - 120)
if Day >= 152 and Day <= 181:
  print("June ", Day - 151)
if Day >= 182 and Day <= 212:
  print("July ", Day - 181)
if Day >= 213 and Day <= 243:
  print("August ", Day - 212)
if Day >= 244 and Day <= 273:
  print("September ", Day - 243)
if Day >= 274 and Day <= 304:
  print("October ", Day - 273)
if Day >= 305 and Day <= 334:
  print("November ", Day - 304)
if Day >= 335 and Day <= 365:
  print("December ", Day - 334)

#Question 4
#I just set b in range for the 5 + 1 rows and c is also in rage 5,0 +b, -1. This means it just sets the rows to 5 right away, instead of having to put a variable, making it a lot easier.
for b in range(5 + 1):
  for c in range(5, 0 +b, -1):
    print(c, end=' ')
  print()

#Question 5
#This is very similar to question 4, however, I had to make the "row" variable which makes it whenever you have a certain number it makes that certain row number.
row = int(input("Pick a number for the row length, "))
#After the question is asked the user inputs their number and it will create a row pattern with the same code as question 4.
for b in range(row + 1):
  for c in range(row, 0 +b, -1):
    print(c, end=' ')
  print()

int(input("Thank you sorry I couldnt get to the bonus question. "))