import string
import random


def generate_id():
    tokens = list(string.ascii_letters + string.digits)
    uid = ''
    for i in range(6):
        uid += random.choice(tokens)
    return uid


class Amazon:
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.order_cart = None
        self.isPrime = 1

    def get_details(self):
        self.id = generate_id()
        self.name = input("Enter Your Name: ")
        self.email = input("Enter Your e-mail Address: ")

    def buy_prime(self):
        self.isPrime = 0

    def buy_items(self):
        self.order_cart = [i for i in input('Enter the Items: ').split(", ")]


user_list = []


def find_user_pos(new_user):
    user_count = len(user_list)
    pos = 0
    for i in range(user_count):
        if user_list[i].isPrime <= new_user.isPrime:
            pos += 1
    return pos


print("\t\t\t\t\t\t\t\t\t\tamazon.in")
print("\t\t\t\t\t\t\t\t\t\t  ⏝   ")
print("=======================================================================================")
print("\t\t\t\t\t\t\t\tWelcome to Amazon Shopping")
ch = 'y'
while ch == 'y':
    new_user = Amazon()
    new_user.get_details()

    op = input("Do You Want to Order ? y/n: ")
    if op == 'y':
        new_user.buy_items()

    op = input("Buy Prime for Faster Delivery and Many More  y/n: ")
    if op == 'y':
        new_user.buy_prime()

    pos = find_user_pos(new_user)
    user_list.insert(pos, new_user)

    ch = input('Want to Add More User ? y/n: ')

# for i in user_list:
#    print(i.name, i.isPrime, i.order_cart)

for i in user_list:
    if i.isPrime == 0:
        print(f'Hi {i.name}, Your Order Has Been Shipped Under Prime Delivery')
    else:
        print(f'Hi {i.name}, Your Order Has Been Shipped')
