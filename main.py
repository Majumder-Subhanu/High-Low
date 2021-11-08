import art
import data
import random
import os


def game(score, val):
    while True:
        random1 = data.data[random.randint(0, 49)]
        random2 = data.data[random.randint(0, 49)]
        if val:
            print("Current score: {0}".format(score))
        else:
            print("Sorry, that's wrong, Final score: {0}".format(score))
            exit(1)
        if random1 != random2:
            print(f"Compare A: {random1.get('name')}, a {random1.get('description')}, from {random1.get('country')}")
            print(art.vs)
            print(f"Compare B: {random2.get('name')}, a {random2.get('description')}, from {random2.get('country')}")
            if random1.get('follower_count') > random2.get('follower_count'):
                actual = "A"
            else:
                actual = "B"
            followers = input("Who has more followers 'A' or 'B': ")
            if followers == actual:
                score += 1
                os.system("cls")
                game(score, True)
            else:
                os.system("cls")
                game(score, False)
                exit(1)


if __name__ == '__main__':
    print(art.logo)
    game(0, True)
