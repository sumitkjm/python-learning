def about (name, age, likes = "listening to music"):
    sentence = "Meet {}! She/He is {} years old and likes {}".format(name,age,likes)
    return sentence;

print (about("Sumit",36,"play badminton!"))

print (about("Sumit",36))

dictionary ={"name":"Manasvi","age":9,"likes":"reading books!"}
print (about(**dictionary))