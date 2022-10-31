
# Code to find an Armstrong number
# 371 is an armstrong numbre
# 3**3 + 7**3 + 1**3 = 371
# 153 is also an armstrong numbe
# 9474= (9x9x9x9)+ (4x4x4x4)+ (7x7x7x7)+ (4x4x4x4)
num = int(input("Enter a number: "))

for i in range(num+1):
    i_str = str(i)
    len_i = len(i_str)
    s = [int(j)**len_i for j in i_str]
    sum = 0
    for k in s:
        sum = k+sum
    if sum == i:
        print(i,'is an armstrong number.')
    # elif sum != i:
    #     print(i,"this is not an armstrong number")