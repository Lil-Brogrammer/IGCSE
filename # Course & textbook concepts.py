# Course & textbook concepts

'''
# Sorting Algorithms
def insertion_sort(n):
    sorted_list = [n[0]]

    for i in range(1, len(n)): 
        sorted_list.append(n[i])
        for x in range(len(sorted_list)-1):
           while sorted_list[i] > sorted_list[x]:
             sorted_list[i], sorted_list[x] = sorted_list[x], sorted_list[i]
           while sorted_list[i] < sorted_list[x]:
             sorted_list[x], sorted_list[i] = sorted_list[i], sorted_list[x]
           
    print(sorted_list)
    
unsorted_numbers = list(map(int, input("Enter the numbers to sort them: ").strip().split()))
insertion_sort(unsorted_numbers)

'''

'''
def merge_sort(n):
   sorted_list = [n[0]]
   # Sort this list, sort as many items as the size of the sorted list, now merge and sort it all.


passes = 0
Names = list(map(str, input("Enter the names: ").strip().split()))

while passes <= len(Names):
    for i in range(len(Names)-1):
      if Names[i][0] > Names[i+1][0]:
          Names[i], Names[i+1] = Names[i+1], Names[i]
      elif Names[i][0] == Names[i+1][0] and Names[i][1] > Names[i+1][1]:
          Names[i], Names[i+1] = Names[i+1], Names[i] 
    passes += 1

print(Names)
'''

'''
# Bubble sort of alphabets - IMPORTANT AND HARD
passes = 0
Names = list(map(str, input("Name plz: ").strip().split()))

while passes <= len(Names):
    for i in range(len(Names)-1):
        changed = False
        if Names[i][0] > Names[i+1][0]:
          Names[i], Names[i+1] = Names[i+1], Names[i]
        if min(Names[i], Names[i+1]) in max(Names[i], Names[i+1]) and len(Names[i]) > len(Names[i+1]):
          Names[i], Names[i+1] = Names[i+1], Names[i] 
        else:
          for j in range(1, min(len(Names[i]), len(Names[i+1]))):
            if  Names[i][0] == Names[i+1][0] and Names[i][j-1] == Names[i+1][j-1] and Names[i][j] > Names[i+1][j] and changed == False:
                Names[i], Names[i+1] = Names[i+1], Names[i]
                changed = True
    passes += 1

print(Names)
'''

''' L8 Programming: String manipulation
stringInput = str(input("Enter a message: "))
for count in range(0, len(stringInput)):
  character = stringInput[count:count+1]
  print(character)
# character = stringInput[len(stringInput)-3:]

print(stringInput.lower())
print(stringInput.upper())
'''

'''
# Assignment 8
weight = float(input("Enter the weight of parcel: ")) 
choice = int(input("Enter your option: "))
endPrompt = False

def calculate_cost(parcel, option):
    global endPrompt
    while endPrompt == False:
        if option == 1 and weight >= 0.5 and weight <= 5:
            print("Guaranteed next day delivery before noon. ")
            cost = parcel*10 + 1
            print("Cost: $", str(cost))
            endPrompt = True
        elif option == 2 and weight >= 0.5 and weight <= 5:
            print("Guaranteed next day delivery. ")
            cost = parcel * 10
            print("Cost: $", str(cost))
            endPrompt = True
        elif option == 3 and weight >= 0.5 and weight <= 5:
            print("24-hour delivery. ")
            print("Cost: $5")
            endPrompt = True
        elif option == 4 and weight >= 0.5 and weight <= 5:
            print("48-hour delivery. ")
            print("Cost: $4")
            endPrompt = True
        elif option == 5 and weight >= 0.5 and weight <= 5:
            print("3-5 days delivery. ")
            print("Cost: $3")
            endPrompt = True
        else:
            parcel = float(input("Parcel should be between 0.5 and 5 kg! "))
            option = int(input("Select between 1 & 5! "))

calculate_cost(weight,choice)
askAgain = str(input("Change? [y/n]: "))
while askAgain == 'y':
    endPrompt = False
    weight = float(input("Enter the weight of parcel: "))
    choice = int(input("Enter your option: "))
    calculate_cost(weight,choice)
    askAgain = str(input("Change? [y/n]: "))
'''

'''
Student = [str(input("name pwese: ")) * 1 for k in range(0, 8)]
Counter = 0

for Counter in range(0, len(Student)):
    print(Student[Counter])
'''

'''
for i in range(0, 2):
    for k in range(1, 5):
        print(k)
'''

'''
#11c
import random
a = random.randint(10, 20)
b = random.randint(10, 20)
quotient = a // b
remainder = a % b
print(a)
print(b)
print("The quotient of a/b is: ", str(quotient))
print("The remainder of a/b is: ", str(remainder))
'''

'''
#12c
board = [['x','o','x'],['x','o','x'],['x','o','x']]
def showBoard(interface):
    for row in range(0,3):
        print(board[row])
showBoard(board)
'''

''' 
#13c
data = "test"
file = open('sample')
file.writelines(data)
file.close()
print(file)
'''

'''
#14b
validPass = False
password = str(input("Set up your password: "))

def checkPassword(word):
    
    global file
    global validPass
    upperCase = 0
    no_spaces = True
    contains_int = False

    for i in range(0, len(word)):
        if word[i] == " ":
            no_spaces = False

    for k in range(0, len(word)):
        if word[k] == word[k].upper() and word[k] != '0' and word[k] != '1' and word[k] != '2' and word[k] != '3' and word[k] != '4' and word[k] != '5' and word[k] != '6' and word[k] != '7' and word[k] != '8' and word[k] != '9':
            upperCase += 1

    for j in range(0, len(word)):
        if word[j] == '0' or word[j] == '1' or word[j] == '2' or word[j] == '3' or word[j] == '4' or word[j] == '5' or word[j] == '6' or word[j] == '7' or word[j] == '8' or word[j] == '9':
            contains_int = True

    if upperCase >= 1 and no_spaces == True and contains_int == True and len(word) >= 10 and len(word) <= 20:
        validPass = True
        file = open('sample', 'w')
        file.writelines(word)
        file.close()
        print("Good password! ")
    if len(word) < 10 or len(word) > 20:
        validPass = False
        print("Password must be between 10 and 20 characters! ")
    if upperCase < 1 or no_spaces == False:
        validPass = False
        print("Your password must include an uppercase letter with no spaces! ")
    if contains_int == False:
        validPass = False
        print("Your password must contain an integer! ")


# 14c

checkPassword(password)


#14a

choice = int(input("Enter your choice (4 to quit): "))

def settings(option):
 
 global password
 global validPass

 def checkNewPassword(word): #For 14d
    file = open('sample')
    originalPassword = file.read()
    if word == originalPassword:
       print("Password matches! ")
    else:
       print("Password doesn't match!")

 def verify(word): # For 14e
    global password
    if word == password:
        password = str(input("Change your original password: "))
        checkPassword(password)
    else:
        print("Incorrect! Password cannot be changed! ")
  

 while option != 4:
    if option == 1:
        validPass = False
        while validPass == False:
            new_password = str(input("Enter a new password: "))
            checkPassword(new_password)
        option = int(input("Enter your choice (4 to quit): "))
    elif option == 2:
        new_password = str(input("Check your password: ")) 
        checkNewPassword(new_password)
        option = int(input("Enter your choice (4 to quit): "))
    elif option == 3:
       confirm_password = str(input("Enter your old password to confirm: "))
       verify(confirm_password)
       option = int(input("Enter your choice (4 to quit): "))

settings(choice)
'''

'''
game_over = False
draw = False

def determine_winner(board):

    global game_over
    global draw

    for i in range(0, len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and len(board[i][0]) != 0:
          game_over = True
          print(board[i][0] + " is the winner! ")

    for j in range(0, len(board)):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] and len(board[0][j]) != 0:
            game_over = True
            print(board[0][j] + " is the winner! ")
            
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and len(board[0][0]) != 0:
        game_over = True
        print(board[0][0] + " is the winner! ")
        
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and len(board[0][2]) != 0:
        game_over = True
        print(board[0][2] + " is the winner! ")

    for k in range(0, 3):
       if (len(board[k][0]) != 0 and len(board[k][1]) != 0 and len(board[k][2]) != 0 and game_over == False):
          draw = True
       else:
          draw = False
    if draw == True:
       print("It's a draw! ")
    
def play_game():
    global Game
    Game = [["", "", ""], ["", "", ""], ["", "", ""]]
    player1position = str(input("x or o? "))
    player2position = str(input("x or o? "))
    turn = 'x'
    while draw == False and game_over == False:
      if turn == player1position:
        row = int(input("enter your row as player1: "))
        column = int(input("enter your column as player1: "))
        if Game[row][column] == "":
          Game[row][column] = player1position
          print(Game)
          determine_winner(Game)
          turn = player2position
      elif turn == player2position:
         row = int(input("enter your row as player2: "))
         column = int(input("enter your column as player2: "))
         if Game[row][column] == "":
           Game[row][column] = player2position
           print(Game)
           determine_winner(Game)
           turn = player1position

play_game()
'''



    
       