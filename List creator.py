import time

list_input=(input("Input your things, whatever you want. (Make sure to separate it with commas.) \n"))

if ',' not in list_input:
    print("Ahh, insert commas, please. Run me again.")
    time.sleep(2)
    quit()

list=[] # '[]' is for blank, which can also be filled.

list.append(list_input) #with the help of .append, we can add any object to the list.

time.sleep(0.5)

print("Your things are - \n", list)