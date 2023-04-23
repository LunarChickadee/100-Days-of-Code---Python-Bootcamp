import random

origin = input('Where are you from? \n')

pet_name = input("What's a name you'd give a pet? \n")

random_num = random.randint(1,2)

if random_num ==1:
    print("Your Bandname is: "+origin+' '+pet_name)
elif random_num == 2:
    print("Your Bandname is: "+pet_name+' '+origin)