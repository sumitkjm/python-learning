#get user email address

email = raw_input("Please provide your email address?: ").strip()

# slice out user name

partition = email.partition('@')
print (partition[0])
# slice domain name
domain = partition[2]
domain1 = email[email.index("@")+1:]
# Format message
formatedMessage = "User Name is {} and Domain is {}".format(partition[0],domain)
print (formatedMessage)
#Display output message


