'''Write  python progrm which will keep adding a stream of numbers inputed by the user,
The adding stops as soon as user presses q key on the keyboard
'''
sum=0
while(True):
    userInput = input("Enter the item price or press q to quit: \n")

    if(userInput!='q'):
        sum= sum + int(userInput)
        print(f"Your Order total so far: {sum}")

    else:
        print(f"Your Total Bill is {sum}. \nThank you for Shopping with us")
        break