# data types

#string

# "hello"
# print("hello"[2])

#integer

# 123
# print(123+45)
# 123_456_789

#float

# 3.14

#boolean

# true
# false

#type
# num = 6
# print(type(num))
#
# print(round(8/3,2))
#
# print(9//2)

#math operator:
# % - remainder
# 5%2 = 1

#f-string
# score = 4
# print(f"your score is {score}")


print("Welcome to tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("how many people will split the bill?\n"))

total_bill = bill + (bill * (tip/100))

each_pay = round(total_bill/ people,2)

print(f"Each person should pay: {each_pay}")