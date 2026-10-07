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