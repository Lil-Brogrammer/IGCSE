from turtle import *
# from tkinter import *
# window = Tk()

# Loop lesson: In pseudocode, FOR loops end when it's false and WHILE loops end when it's true + the condition statement is inverted

'''
# Practice Task 8.1
for _ in range(6):
    forward(100)
    right(60)

mainloop()
'''

'''
# Practice Task 8.2 

title("Practice Task 8.2")

for _ in range(6):
    for _ in range(4):
       forward(100)
       left(90)
    right(60)
    
    
mainloop()
'''

'''
# Demo Task 8.1

window.title('Demo Task 8.1 app')
label = Label(window, width=10, height=1, text='Enter number: ')
label.grid(row=0, column=0)
entry = Entry(window, width=10)
entry.grid(row=1, column=0)

def produce():
  new_entry = int(entry.get())
  for i in range(1, 11):
    new_label = Label(window, width=10, height=1, text=str(new_entry*i))
    new_label.grid(row=i+2, column=0)

button = Button(window, width=10, height=1, text='Get multiples', command=produce)
button.grid(row=1, column=2)

window.mainloop()
'''

""" 
# 8.3 Exercise b

number_input = int(input("Enter a number below 10: "))
for i in range(1, number_input+1):
    square = i**2
    print("number: " + str(i) + "     square: " + str(square))
"""

""" 
# 8.4 Exercise b

number_input = int(input("Enter a number below 10: "))
for i in range(1, number_input+1):
    bit_value = 2**(i-1)
    print("bit number: " + str(i) + "     bit value: " + str(bit_value))
"""

'''
# 8.5 Exercise b 
# Exercise c: Yellow Jolly Chair Swallows Tasty Sand end
word = str(input("Enter the word: "))
text = ''

while word != 'end':
    text = text + ' ' + word
    word = str(input("Enter the word: "))
if word == 'end':
    print(text)
'''

'''
window.title("Challenge Task 8.1")
sentence = ''
my_text_entry_box = Entry(window, width=25)
my_text_entry_box.grid()
output_label = Label(window, width=len(sentence), height=1, text='')
output_label.grid()

def submit_word():
    global sentence 
    word = my_text_entry_box.get()

    if word != 'end':
        sentence = sentence + word + ' '
        my_text_entry_box.delete(0, END)
        output_label.config(text=sentence)
    else:
        output_label.config(text=sentence)

submit = Button(window, width=25,text='Submit ', command=submit_word)
submit.grid()

window.mainloop()
'''

'''
# Practice Task 8.6 

counter = 1
sum = 0
number = int(input())
sum = sum + number

while counter < 20 and number != -1:
    number = int(input())
    sum += number
    counter += 1
    if number == -1:
        sum = sum - number
        counter = counter - 1

print("The average is: " + str(sum/counter))
'''

'''
# Practice Task 8.7

while True: 
    password1 = str(input("password pwese: "))
    password2 = str(input("again pwese uwu :) "))
    if password1 == password2 and len(password1) > 10:
        print("Password accepted")
        break
    else:
        print("Error!") 
'''

'''
# Practice Task 8.8a

total = 0
number = int(input())

while number != -1:
    total += number
    number = int(input())

print(total)
'''

'''
# Practice Task 8.8b

total = 0

while True:
    number = int(input())
    total = total + number 
    if number == -1:
        break
    total += 1

print(total)
'''

'''
# End-of-chapter Task 2b
number = int(input("Enter a number to find its factors: "))
factor = []
counter = 1

for counter in range(1, number+1):
    if number % counter == 0:
        factor.append(counter)

print(factor)
'''

'''
# End-of-chapter Task 3
size = int(input("Enter size between 3 and 10: "))
if size >= 3 and size <= 10:
    for i in range(5):
        right(72)
        forward(size)

mainloop()
'''

'''
# End-of-chapter Task 4
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter the 2nd number: "))

factor = []
counter = 1

for counter in range(1, min(number1, number2)+1):
    if number1 % counter == 0 and number2 % counter == 0:
        factor.append(counter)

print(factor)
'''

#'''
# End-of-chapter Task 5b...too complicated but simple version is found in pseudocode from notebook 
n = int(input())
series = []

for i in range(0, n):
    if len(series) == 0:
        series.append(0)
    elif len(series) == 1:
        series.append(series[0] - (series[0] - 1))
    else:
      number = series[i-1] + series[i-2]
      series.append(number)

print(series)
#'''