






#2 davaleba

first_num = int(input("enter your first number: "))




next_nums = int(input("enter your next number "))
tries = 100000000000000

num = [first_num , next_nums]

while next_nums > 0 and tries > -100000:
    print(num)

    tries -= 1

    next_nums -=1


