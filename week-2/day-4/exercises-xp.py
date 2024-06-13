import random

#exercise 1
def display_message():
    print("I'm learning Python")
display_message()


#exercise 2
def favorite_book(title):
    print(f'My favorite book is {title}')

favorite_book('Harry Potter')

#exercise 3

def describe_city(city, country = 'China'):
    print(f"{city} is in {country}")

describe_city("Xinjiang")

#exercise 4

user_number = int(input('Enter a number between 1 and 100: '))
random_number = random.randint(1, 100)

if random_number == user_number:
    print("Great success!!")
else: 
    print(f"Numbers don't match: {random_number} does not equal {user_number}")

#exercise 5

def make_shirt(size, text = "I love Python"):
    print(f"The size {size} shirt will read: '{text}'.")

make_shirt("Large")
make_shirt("Medium")
make_shirt(16, "Occupy Mars")

#exercise 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)

def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + " the Great"

make_great()
show_magicians()

#exercise 7

def get_random_temp(season):
    if season == 'Winter':
        return random.randint(-10, 16)
    elif season == 'Summer':
        return random.randint(25, 40)
    else:
        return random.randint(16, 28)

print(get_random_temp('Summer'))

def main():
    season = input("Enter the current season: ")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Freeze your water outside")
    elif temp < 16:
        print("Wear a coat")
    elif temp < 24:
        print("Perfect for a run")
    elif temp < 33:
        print("Make an awesome BBQ pool party")
    else:
        print("We recommend staying in the AC")

main()

#exercise 8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

correct_answers = 0
wrong_answers_count = 0
wrong_answers = []

for question in data:
    user_answer = input(question["question"])
    if user_answer == question["answer"]:
        correct_answers += 1
    else:
        wrong_answers.append({"Question": question["question"], "Your Answer": user_answer, "Correct Answer": question["answer"]})
        wrong_answers_count += 1

print(f"You got {correct_answers} answers correct and {wrong_answers_count} wrong")
print("Here are the questions you got wrong: ", wrong_answers)


