def fizzBuzz():
    user_input = input("input a number between 1 and 100: ")
    try: 
        int(user_input)
    except: 
        print('You must enter a number')
        return fizzBuzz()
    number = int(user_input)
    if number < 1 or number > 100:
        print('Number must be between 0 and 100')
        return fizzBuzz()
    result_str = ""
    if number % 3 == 0: 
        result_str += "Fizz"
    if number % 5 == 0:
        result_str += "Buzz"
    if result_str: 
        print(result_str)
    else:
        print('Thanks')

fizzBuzz()