# Code to find an Armstrong number
# 371 is an armstrong numbre
# 3**3 + 7**3 + 1**3 = 371
# 153 is also an armstrong numbe
# 9474= (9x9x9x9)+ (4x4x4x4)+ (7x7x7x7)+ (4x4x4x4)

num = input("Enter a number: ")
len_num = len(num)
s = [int(i)**len_num for i  in num]
sum = 0
for i in s:
    sum = i+sum

int_num = int(num)
if int_num == sum:
    print("This is an armstrong number.")
else:
    print("This is not an armstrong number.")

