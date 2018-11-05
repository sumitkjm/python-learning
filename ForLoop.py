for number in range (1, 10):
    print (number)

vowels = 0
consonents = 0

word = input("Type any word").strip()

for letter in word:
    if letter.lower() in "aeiou":
        vowels = vowels +1
    else:
        consonents = consonents + 1

print ("Number of Vowels {}".format(vowels))
print ("Number of consonents {}".format(consonents))

students = {"male":["Sumit","Darsh"],
            "female":["Archana","Manasvi"]}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print (name)
