
my_name = input("enter your name:")
my_age = input("enter your age:")
my_addreas = input("enter your addreas:")

if type(my_name)==str :
    if my_age.isdigit():
        print("Hello Mr/Ms" + my_name + "age" + my_age + "located in "+
              my_addreas + "thinks for being one of our  communty, enjoy")
    else:
        print("Error!")
else:
    print("Error!")



