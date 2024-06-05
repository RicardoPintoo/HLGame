import game_data
import art
import random
import os

print(art.logo)

score = 0
winning = True

while winning:
    random_element_a = random.choice(game_data.data)
    random_element_b = random.choice(game_data.data) 

    while random_element_a == random_element_b:
        random_element_a = random.choice(game_data.data)  

    print("Compare A: " + random_element_a['name'])
    print(art.vs)
    print("Against B: " + random_element_b['name'])

    user_input = input("Who has more followers type 'A' or 'B' : ")

    if(random_element_a['follower_count'] > random_element_b['follower_count']):
        if(user_input == 'A'):
            score +=1
            print("You're right !  Current score : " + str(score))
        else:
            print("Sorry that's wrong. Final score : " + str(score))
            winning = False
    else:
        if(user_input == 'B'):
            score +=1
            print("You're right ! Current score : " + str(score))
        else:
            print("Sorry that's wrong. Final score : " + str(score))
            winning = False
    #os.system('cls' if os.name == 'nt' else 'clear')



