import inquirer, random
my_health = 60
zombi_health=15
while True:
    questions = [
    inquirer.List('number',
                message="Reqem sech",
                choices=[1, 2, 3, 4, 5],
            ),
    ]
    answers = inquirer.prompt(questions)
    my_choice=answers["number"]
    zombi_choice = random.randint(1,5)
    print("Zombinin sechimi",zombi_choice)
    
    if my_choice == zombi_choice:
        zombi_health-=my_choice
        print("Zombi cani",zombi_health)
    else:
        my_health-=zombi_choice
        print("Menim canim",my_health)
    if my_health<=0 or zombi_health<=0:
        if my_health<=0:
            print("Zombi uddu")
        elif zombi_health<=0:
            print("Men uddum")
        exit()
        
       
   