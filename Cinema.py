films = {"Finding Dory": [3, 5],
         "Bourne": [18, 5],
         "Ghost Rider": [12, 5],
         "Tarzan": [18, 2]}

while True:
    choice = raw_input("What films what do you want to watch?:").strip()
    if choice in films:
        age = input("How old are you?:")
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print "Enjoy the film"
                films[choice][1] -= 1
            else:
                print "Sorry movie is sold out, better luck next time!"
        else:
            print "You are too young to see the film"
    else:
        print "We don't have that film..."
