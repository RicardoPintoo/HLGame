import game_data
import art
import random
import os

print(art.logo)

score = 0
winning = True
element_a = random.choice(game_data.data)
element_b = random.choice(game_data.data)

while winning: 

    element_a = element_b
    element_b = random.choice(game_data.data)

    while element_a == element_b:
        element_b = random.choice(game_data.data)

    print("Compare A: " + element_a['name'])
    print(art.vs)
    print("Against B: " + element_b['name'])

    user_input = input("Who has more followers type 'A' or 'B' : ")



    if(element_a['follower_count'] > element_b['follower_count']):
        if(user_input == 'A'):
            score +=1
            print("\n # You're right ! Current score : " + str(score))
        else:
            print("\n Sorry that's wrong. Final score : " + str(score))
            winning = False
    else:
        if(user_input == 'B'):
            score +=1
            print("You're right ! Current score : " + str(score))
            #element_b = random.choice(game_data.data)
        else:
            print("Sorry that's wrong. Final score : " + str(score))
            winning = False
    #os.system('cls' if os.name == 'nt' else 'clear')



