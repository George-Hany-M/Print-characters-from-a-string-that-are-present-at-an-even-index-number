# George Hany
# Write a program to accept a string from the user and display characters that are present at an even index number.

# input the string from the user
str = input('Original String Is : ')

# get the length of the string
length = len(str)

print('Printing Only Even Index Chars :')

# iterate in each charachter in the string from 0 to length - 1
for index in range(length):
    if index % 2 == 0:
        print(str[index])