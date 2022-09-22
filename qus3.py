numbers =[]
for i in range (5):
    my_input = int(input("enter a number:"))
    numbers.append (my_input)
print(numbers)
print("Big number is:",max(numbers))
print("min number is:",min(numbers))