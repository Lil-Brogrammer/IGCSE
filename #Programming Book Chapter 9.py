# from tkinter import *
# window = Tk()
from turtle import *
import turtle

'''
# Practice Task 9.3d
average = 0
sum = 0
count = 1
number = int(input("Enter the number of pages: "))

while True:
    sum = sum + number
    average = sum / count
    number = int(input("Enter the number of pages: "))
    count += 1
    if number < 0:
        print(f"Average number of pages: {average}")
        break
'''

'''
# Challenge Task 9.2
sum = 0

while True:
    rainfall = float(input("Enter the rainfall amount (to the nearest 0.1 mm): "))
    sum = sum + rainfall.__round__(1)
    if rainfall < 0:
        print(f"Total rainfall: {sum}")
        break
'''

'''
# End-of-chapter Task 1
weather = float(input("Enter the temperature in Celsius: "))
count = 0
sum = 0

while True:
    sum += weather 
    count += 1
    weather = float(input("Enter the temperature in Celsius: "))
    if weather == -1:
        average = sum / count
        print(f"Average temperature: {average}")
        break
'''

'''
# End-of-chapter Task 2a
count = 0
sum = 0
score = int(input("Enter the score: "))

while score != -1 and count <= 100:
    sum += score
    count += 1
    score = int(input("Enter the score: "))

print(sum)
'''

'''
# End-of-chapter Task 2b
display = Label(window, text="Score: ")
output = Label(window, text="0")
display.grid()
output.grid()
score = 0

def change_output():
    global score
    score += 1
    output.config(text=str(score))

button = Button(window, text="SCORE!", width=10, command=change_output)
button.grid()
finish = Button(window, text="Finish", width=10, command=window.destroy)
finish.grid()

window.mainloop()
'''

'''
# End-of-chapter Task 3c

# Drawing the roof...
left(33)
forward(200)
right(66)
forward(200)
right(180-33)
goto(0, 0)


# Drawing the house
left(90)
forward(200)
left(90)
forward(335) #Don't know why this is 335...wanna change it to goto() command but it doesn't work
left(90)
forward(200)

# Drawing the door
right(180)
forward(200)
right(90)
forward(40)
right(90)
forward(160)
left(90)
forward(80)
left(90)
forward(160)

# Drawing the window
right(90)
forward(80)
right(90)
turtle.pencolor("white")
forward(90)
turtle.pencolor("black")
for _ in range(2):
    forward(70)
    left(90)
    forward(90)
    left(90)

turtle.mainloop()
'''