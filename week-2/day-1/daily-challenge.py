import random
userText = input("Type in a string: ")
if len(userText) > 10:
    print('String too long')
elif len(userText) < 10: 
    print('String too short')
else: 
    print("Perfect String!")
    print(userText[0], userText[-1])
    for i in range(len(userText)+1): 
        print(userText[0:i])

    userTextCharList = list(userText)
    random.shuffle(userTextCharList)
    print(userTextCharList)