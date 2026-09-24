from tkinter import *
window = Tk()
'''
# Not my code obv but it is soo cool...got this from Oxford Philosophy course site 
# Planning to use this program for chapter 5 in my programming textbook
from turtle import *

def triangle(size):
    if size > 1:
        forward(size)
        triangle(size/2)
        right(120)
        forward(size)
        triangle(size/2)
        right(120)
        forward(size)
        triangle(size/2)
        right(120)

triangle(100)
mainloop()
'''

# from tkinter import *
# window = Tk()
'''
# Practice task 7.1

discount = 0.5
ticket_price = float(input("Enter the ticket price: "))

for_child = str(input("Is it for a child (Y/N)? "))
if for_child == "Y":
    ticket_price = ticket_price * discount

print(ticket_price)
'''

'''
# Practice task 7.4 


number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

if number1 == number2:
    print("Match")
else:
    print("No Match")
'''

'''
# Practice task 7.5 part 'b'

another_number1 = float(input("Enter a number: "))
another_number2 = float(input("Enter another number: "))

if another_number2 > (2 * another_number1):
    print("Too Large")
else: 
    print("Acceptable")
'''

'''
# Practice task 7.6 

integer1 = int(input("Enter an integer: "))
integer2 = int(input("Enter another integer: "))

if integer2 % integer1 == 0:
    print("Factor")
else: 
    print("Not a Factor")
'''

# Challenge task 7.2

# window = TK()

'''
# GUI of Practice task 7.4

window.title("Match")

number1 = Entry(window, width=30)
number1.grid(row=0, column=1)
number2 = Entry(window, width=30)
number2.grid(row=1, column=1)
match_label = Label(window, width=25, height=1, text="")
match_label.grid(row=2, column=1)


def check_numbers():
    num1 = number1.get()
    num2 = number2.get()
    if num1 == num2:
        match_label.config(text="Match")
    else:
        match_label.config(text="No Match")

def clear_all():
    number1.delete(0, END)
    number2.delete(0, END)
    
submit = Button(width=6, height=1, text="Submit", command=check_numbers)
submit.grid(row=3, column=1)
clear = Button(width=6, height=1, text="Clear", command=clear_all)
clear.grid(row=4, column=1)

window.mainloop()
        '''

'''
# GUI of Practice task 7.5
window.title("Too Large")

another_number1 = Entry(window, width=30)
another_number1.grid(row=0, column=1)
another_number2 = Entry(window, width=30)
another_number2.grid(row=1, column=1)
another_match_label = Label(window, width=25, height=1, text="")
another_match_label.grid(row=2, column=1)


def another_check_numbers():
    another_num1 = int(another_number1.get())
    another_num2 = int(another_number2.get())
    if another_num2 > (2 * another_num1):
        another_match_label.config(text="Too Large")
    else:
        another_match_label.config(text="Acceptable")

def another_clear_all():
    another_number1.delete(0, END)
    another_number2.delete(0, END)

another_submit = Button(width=6, height=1, text="Submit", command=another_check_numbers)
another_submit.grid(row=3, column=1)
another_clear = Button(width=6, height=1, text="Clear", command=another_clear_all)
another_clear.grid(row=4, column=1)

window.mainloop()
'''

'''
# Practice task 7.8   


age = int(input("Enter the age of the passenger: "))
price = float(input("Enter the price of the ticket: "))

if age >= 18:
    print("Final cost: ", str(price))
else:
    if age < 18 and age >= 15:
        price = price - 0.2 * price
        print("Final cost: ", str(price))
    else: 
        if age < 15 and age >= 4:
            price = price - 0.4 * price
            print("Final cost: ", str(price))
        else:
            price = 0
            print("Ticket is free. ")
'''

'''
# Practice Task 9b

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month31 = [month[0], month[2], month[4], month[6], month[7], month[9], month[11]]
month30 = [month[3], month[5], month[8], month[10]]

name = str(input("Enter the month name: "))

if name in month31:
    print(31)
elif name in month30:
    print(30)
else:
    print(28)
'''

'''
# Practice Task 10b
window.title("Practice Task 10b")
yob = Entry(window, width=25, text='Enter year: ')
yob.grid()
output = Label(window, width=25, height=1, text='')
output.grid()

def findYear():
    new_yob = int(yob.get())

    if new_yob % 4 == 0:
        if new_yob % 100 == 0:
            if new_yob % 400 == 0:
                output.config(text="Leap Year")
                output.grid()
            elif new_yob % 400 != 0:
                output.config(text="Normal Year")
                output.grid()
        elif new_yob % 100 != 0:
            output.config(text="Leap Year")
            output.grid()
    elif new_yob % 4 != 0:
        output.config(text='Normal Year')
        output.grid()


output_button = Button(window, width=25, height=1, text='Find Year', command=findYear)
output_button.grid()


window.mainloop()
'''

'''
# Practice Task 11
window.title("Practice Task 10b")
yob = Entry(window, width=25, text='Enter year: ')
yob.grid()
output = Label(window, width=25, height=1, text='')
output.grid(row=2, column=0)

def findYear():
    
    new_yob = int(yob.get())

    if new_yob % 4 == 0 and (new_yob % 100 != 0 or new_yob % 400 == 0):
      output.config(text="Leap Year")
      output.grid(row=2, column=0)
    else:
      output.config(text="Normal Year")
      output.grid(row=2, column=0) 

output_button = Button(window, width=25, height=1, text='Find Year', command=findYear)
output_button.grid(row=1, column=0)


window.mainloop()
'''

'''
# End-of-chapter Task 1b

first = str(input("Enter the first number: "))
second = str(input("Enter the second number: "))
third = str(input("Enter the thrid number: "))

if first == second or first == third or second == third:
    if first == second:
        print("Error")
    else:
        if first == third:
            print("Error")
        else:
            if second == third:
               print("Error")
else:
    print(max(first,second,third))
'''

'''
# End-of-chapter Task 1b

first = str(input("Enter the first number: "))
second = str(input("Enter the second number: "))
third = str(input("Enter the thrid number: "))

if first == second:
    print("Error")
elif first == third:
    print("Error")
elif second == third:
    print("Error")
else:
    print(max(first,second,third))
'''

'''
# End-of-chapter Task 2b

mode = str(input("Enter the class: "))

price = 0

def economy_price(location, way, meal):
    if location.lower() == "edinburgh":
      if way == 1:
        if meal == 'y':
            price = 32+12
        else:
            price = 32
      else:
        if meal == 'y':
            price = 52+18
        else:
            price = 52
    else:
        if way == 1: 
          if meal == 'y':
            price = 36+12
          else:
            price = 36
        else:
          if meal == 'y':
            price = 50+18
          else:
            price = 50

    print(price)


def business_price(location, way):
    if way == 1:
      if location.lower() == "edinburgh":
        price = 87
    
      else:
        price = 72
    else:
      if location.lower() == "edinburgh":
        price = 138
      else:
        price = 178

    print(price)


if mode.lower() == "economy":
    preferred_location = str(input("Enter location: "))
    preferred_way=int(input("one way or two way? "))
    preferred_meal=str(input("meal yes or no? [y/n] "))
    economy_price(preferred_location, preferred_way, preferred_meal)
else:
    preferred_way=int(input("one way or two way? "))
    preferred_location = str(input("Enter location: "))
    business_price(preferred_location, preferred_way)
'''

'''
# End-of-chapter task 2c

window.title("Practice Task 2c")

options = ('Business', 'Economy')
set_options = StringVar()
set_options.set('Class: ')
menu = OptionMenu(window, set_options, *options)
menu.grid()



new_location = Entry(window, width=25, text="Enter the location: ")
new_location.grid()
location_text = Label(window, text="Enter the location: ")
location_text.grid()
new_way = Entry(window, width=25)
new_way.grid()
way_text = Label(window, text="Enter the type of journey: ")
way_text.grid()
new_meal = Entry(window, width=25)
new_meal.grid()
meal_text = Label(window, text="Do you want meals? [y/n] ")
meal_text.grid()

price = Label(window, width=25, text='0')
price.grid()

def ticket():
    meal = str(new_meal.get())
    location = str(new_location.get())
    way = str(new_way.get())
    mode = set_options.get()

    if location.lower() == 'edinburgh' and way == '1' and mode == 'Economy' and meal == 'y':
        price.config(text=str(32+12))
        
    elif location.lower() == 'edinburgh' and way == '1' and mode == 'Economy' and meal == 'n':
        price.config(text='32')
    elif location.lower() == 'edinburgh' and way == '2' and mode == 'Economy' and meal == 'y': 
        price.config(text=str(52+18))
    elif location.lower() == 'edinburgh' and way == '2' and mode == 'Economy' and meal == 'n':
        price.config(text='52')

    elif location.lower() == 'cardiff' and way == '1' and mode == 'Economy' and meal == 'y':
        price.config(text=str(36+12))
    elif location.lower() == 'cardiff' and way == '1' and mode == 'Economy' and meal == 'n':
        price.config(text='36')
    elif location.lower() == 'cardiff' and way == '2' and mode == 'Economy' and meal == 'y':
        price.config(text=str(50+18))
    elif location.lower() == 'cardiff' and way == '2' and mode == 'Economy' and meal == 'n':
        price.config(text='50')

    elif location.lower() == 'edinburgh' and way == '1' and mode == 'Business':
        price.config(text='87')
    elif location.lower() == 'edinburgh' and way == '2' and mode == 'Business':
        price.config(text='178')
    elif location.lower() == 'cardiff' and way == '1' and mode == 'Business':
        price.config(text='72')
    elif location.lower() == 'cardiff' and way == '2' and mode == 'Business':
        price.config(text='138')


calculate = Button(window, width=25, text='Calculate cost', command=ticket)
calculate.grid()

window.mainloop()
'''