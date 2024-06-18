#exercise 1
from typing import Union
import random, string, datetime

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __add__(self, other: Union["Currency", int]):
        if isinstance(other, Currency):
            if other.currency == self.currency:
                return self.amount + other.amount
            else:
                raise ValueError("Cannot add different currencies")
            
        elif isinstance(other, int):
            return self.amount + other
    def __iadd__(self, other: Union["Currency", int]):
        if isinstance(other, Currency):
            if other.currency == self.currency:
                self.amount = self.amount + other.amount
                return self
            else:
                raise ValueError("Cannot add different currencies")
            
        elif isinstance(other, int):
            self.amount = self.amount + other
            return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
    
print(str(c1))
#'5 dollars'

print(int(c1))
#5

print(repr(c1))
#'5 dollars'

print(c1 + 5)
#10

print(c1 + c2)
#15

print(c1) 
#5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
#20 dollars

# c1 + c3
#error

#exercise 2 see ./exercise_two.py


#exercise 3

print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)))

# exercise 4
def current_date():
    return datetime.date.today()

print(current_date())

#exercise 5
def time_to_january():
    timeamount = datetime.datetime(2025, 1, 1) - datetime.datetime.now()
    print(f"The 1st of January is in {timeamount.days} days and{str(timeamount).split(',')[1].split('.')[0]} hours")


#exercise 6
def minutes_lived():
    birthday = input("Enter your birthday and time of birth (DD/MM/YYYY HH:MM): ")
    birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y %H:%M")
    time_elapsed = datetime.datetime.now() - birthday
    print("Minutes lived: ", time_elapsed.total_seconds() / 60)
    return time_elapsed.total_seconds() / 60

minutes_lived()

#exercise 7

from faker import Faker
fake = Faker()

users = []
def create_new_users(number):
    for i in range(number):
        users.append({
            "name": fake.name(), 
            "adress": fake.address(), 
            "langage_code": fake.language_code()
        })

create_new_users(10)
print(users)


