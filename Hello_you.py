#Ask User Name
userName = raw_input ("What's your name?: ").strip()
#Ask User Age
age = input( "What's your age?: ")
#Ask User City
city = raw_input ("What's your City?:").strip()
#Ask User what they enjoy
love = raw_input("what you love to do?:")
#Create output text
#output = userName + " " + str(age) + " " + city +" " + love
#Print output on the screen
output = "{} - {} - {} - {}".format(userName,age,city,love)
print (output)
# print (userName)
# print (type(age))
# print (city)
# print (love)
