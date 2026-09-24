'''
# Programming Task 8.1

name = str(input("Please enter your legal name: ")) 
print("Legal name:", name)
acc_type = input("Is this your personal account? [Leave it if it's not...] ")
print("Personal Account:", bool(acc_type))

dob_month = int(input("Please enter your month of birth: "))
if dob_month > 12 or dob_month < 1: 
    print("Please enter a valid month: ")
    dob_month = int(input())
    print('Month of birth:' + dob_month)
else:
    print(dob_month)

dob_date = int(input("Please enter your date of birth: "))
if dob_date > 31 or dob_date < 1:
    print("Please enter a valid date: ")
    dob_date = int(input())
    print(dob_date)
else:
    print(dob_date)

dob_year = int(input("Please enter your year of birth: "))
if len(str(dob_year)) != 4:
    print("Please enter a valid year: ")
    dob_year = int(input())  
    print(dob_year)
else:
    print(dob_year)

username = str(input("Please enter your desired username: "))
if len(username) < 8:
    print("please enter a username with at least 8 characters: ")
    username = str(input())

print(acc_type)
'''

'''
# Programming Task 8.2

num1 = float(input("One number pwese: "))
op = str(input("operation pls: "))
while op != '+' and op != '-' and op != 'x' and op != '/' and '^' and '%': 
    op = str(input("Please enter a valid operation: "))
num2 = float(input("Another one pwese: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == 'x':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '^':
    print(num1 ^ num2)
elif op == '%':
    print(num1 % num2)
'''

'''
# Programming Task 8.3

number = int(input("Enter a number between 1 to 10 for the user to guess: "))
guess = int(input("Guess: "))
count = 0

while guess != number:
    count += 1
    if guess < number:
        print("think higher...")
    else:
        print("think lower...")
    guess = int(input("Guess: "))
else:
    print("Good. ", "It took you", count, "tries!")
'''    

'''
# File handling
file = open('sample', 'w')
file.writelines("benJeff99ben")
file.close()
file = open('sample')
print(file.read())
'''

'''
# Programming Task 8.4

rounds = int(input("How many rounds do you wanna grind? "))
count = 0
x_score = 0
o_score = 0
game_over = False
draw = False

def determine_winner():

    global game_over
    global draw
    global x_score
    global o_score

    for i in range(0, len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and len(board[i][0]) != 0:
          game_over = True
          print(str(board[i][0]) + " is the winner! ")
          if board[i][0] == 'x':
             x_score += 1
          elif board[i][0] == 'y':
             o_score += 1

          
        
    for j in range(0, len(board)):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] and len(board[0][j]) != 0:
            game_over = True
            print(str(board[0][j]) + " is the winner! ")
            if board[0][j] == 'x':
              x_score += 1
            elif board[0][j] == 'y':
              o_score += 1
            
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and len(board[0][0]) != 0:
        game_over = True
        print(str(board[0][0]) + " is the winner! ")
        if board[0][0] == 'x':
            x_score += 1
        elif board[0][0] == 'y':
            o_score += 1
       
        
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and len(board[0][2]) != 0:
        game_over = True
        print(str(board[0][2]) + " is the winner! ")
        if board[0][2] == 'x':
            x_score += 1
        elif board[0][2] == 'y':
            o_score += 1
       

    for k in range(0, 3):
       if (len(board[k][0]) != 0 and len(board[k][1]) != 0 and len(board[k][2]) != 0 and game_over == False):
          draw = True
       else:
          draw = False
    if draw == True:
       print("It's a draw! ")
    
def play_game():
    global board
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player1position = str(input("x or o? "))
    player2position = str(input("x or o? "))
    turn = 'x'
    while draw == False and game_over == False:
      if turn == player1position:
        row = int(input("enter your row as player1: "))
        column = int(input("enter your column as player1: "))
        if board[row][column] == "":
          board[row][column] = player1position
          print(board)
          determine_winner()
          turn = player2position
      elif turn == player2position:
         row = int(input("enter your row as player2: "))
         column = int(input("enter your column as player2: "))
         if board[row][column] == "":
           board[row][column] = player2position
           print(board)
           determine_winner()
           turn = player1position
       

while count < rounds:
   play_game()
   game_over = False
   draw = False
   count += 1

if x_score > o_score:
   print("Final winner is: x! ")
elif o_score > x_score:
   print("Final winner is: o! ")
else:
   print("Final result: It's a draw! ")
'''


