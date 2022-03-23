from http.client import TEMPORARY_REDIRECT
import time

def print_pause(message_here):
    print(message_here)
    time.sleep(2)

print_pause("Welcome to the Big Apple!")
print_pause("Where we don't actually grow apples.")
print_pause("But we got plenty of rats!")
print_pause("Here we either take the train or we take a cab to get where we gotta go.")
while True:
    while True:
        response = input("So, what we taken?\n").lower()
        if "cab" in response:
            print_pause("Great, good luck finding one in this weather!")
            break
        elif "train" in response:
            print_pause("Alright, but we gotta hurry, I hear the next one coming!")
            break
        else:
            print_pause("Sorry, I don't speak stupid.")
    print_pause("Let's go we're gonna be late.")
    while True:
        try_again = input("Wait, you sure? There's no telling what can happen out there.\nAnswer 'yes' or 'no'.\n").lower()
        if "no" in try_again:
            print_pause("Ok, bye")
            break
        elif "yes" in try_again:
            print_pause("Alright, alright, I hear you.")
            break
        else:
            print_pause("Sorry, I don't speak stupid.")