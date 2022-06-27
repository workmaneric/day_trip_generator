import random

destinations = ["China", "Luxembourg", "Beloit"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def user_destination ():
    random_destinaitons = random_item_picker(destinations)
    user_input = input(f'would you like to go to {random_destinaitons}  y/n ')
    if user_input == "y":
        print(f'You have confirmed that you would like to stay in {random_destinaitons}')
    elif user_input == "n":
        return user_destination()
confirmed_destination = user_destination()