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

