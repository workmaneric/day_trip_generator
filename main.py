import random

destinations = ["China", "Luxembourg", "Beloit", "Canada", "Saginaw", "Antarctica"]
restaurants = ["Chilis", "Subway", "Mcdonalds", "In n Out", "KFC" ]
transport = ["Car", "Bicycle", "Unicycle", "Horse", "Segway", "Jet Pack"]
entertainment = ["Museum", "Music festival", "Yacht race", "Chill walk in the park", "Wine Bar" ]

print("Lets plan a day trip!")

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def user_selection (list):
    random_selection = random_item_picker(list)
    user_input = input(f'Would you like {random_selection}?  y/n ')
    if user_input == "y":
        print(f'You have confirmed that you would like {random_selection}')
        return random_selection
    elif user_input == "n":
        return user_selection(list)
confirmed_destination = user_selection(destinations)
confirmed_restaurant = user_selection(restaurants)
confirmed_transport = user_selection(transport)
confirmed_entertainment = user_selection(entertainment)
print(f'You will be traveling to {confirmed_destination} where you will eat the finest cuisine at {confirmed_restaurant} traveling by {confirmed_transport} and then relaxing by going to a {confirmed_entertainment}')

