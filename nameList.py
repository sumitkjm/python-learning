known_users = ["Sumit","Amit","Dishu","Manshu","Archana","John","Merry"]

print (len(known_users))


while True:
    print ("Hi My Name is Sumit:")
    name = raw_input("What's your name?: ").strip()

    if name in known_users:
        print "Hello {}!".format(name)
        remove = raw_input("Hello good to hear about ou again, would you like ot remove your name from list y/n?")

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print ("I don't think we have met yet!")
            known_users.append(name)

    else:
        print "Name not recognized!"


