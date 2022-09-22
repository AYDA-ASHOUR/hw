first_number = int(input("Enter the first number:"))
print(" 1_ + \n 2_ - \n 3_ * \n 4_ / \n 5_ ^ \n 6_ %")
operation = input("Enter the operation:")
second_number = int(input("Enter the second number:"))
if (operation == "1") or (operation == "+"):
  result = first_number + second_number
elif (operation == "2") or (operation == "-"):
  result = first_number - second_number

elif (operation == "3") or (operation =="*"):
  result = first_number * second_number

elif (operation == "4") or (operation =="/"):
  result = first_number / second_number
elif (operation == "5") or (operation == "^"):
  result = first_number ^ second_number
elif (operation == "6") or (operation == "%"):
  result = first_number % second_number
else:
  print("valid input")

print(result)

print("do you want \n 1- Round the number. \n 2- take the number without , \n 3- exit?")
select_num = int(input("pleas select 1, 2 or 3"))
if select_num == 1 :
  print(round(result))
elif select_num == 2:
  result = str(result)
  result = result.split(".")
  result = result[0]
  print(result)
elif select_num == 3:
  print("Goodbye")