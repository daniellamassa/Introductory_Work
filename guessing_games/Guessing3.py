secretnumber = int(input("Pick a number between 1-100?"))

x=100
y=100
counter = 1
while x != secretnumber:
    answer = input("Is your number greater than ", x/2, "?")
    if (answer == "yes"):
        y =y //(2)


    counter+=1
