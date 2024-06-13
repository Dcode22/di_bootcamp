code_string = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

decoded_string = ""

for i in range(3):
    for string in code_string:
        if string[i].isalpha():
            decoded_string = decoded_string + string[i]
        else: 
            decoded_string = decoded_string + ' '

print(decoded_string)