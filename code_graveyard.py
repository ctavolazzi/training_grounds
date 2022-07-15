# # Weight Converter
# weight = float((input("Weight: ")))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#   converted = weight / 0.45
#   print("Weight in Lbs: " + str(converted))
# else:
#   converted = weight * 0.45
#   print("Weight in Kgs: " + str(converted))

# i = 1
# while i <= 1000:
#   print(i)
#   i+=1



# # Coin Toss Machine
# import random

# heads_counter = 0
# tails_counter = 0

# while heads_counter + tails_counter <= 1000:
#     a= random.randint (1,2)
#     if a==1:
#         heads_counter+=1
#         print ("heads",heads_counter)

#     else:
#         tails_counter+=1
#         print ("tails",tails_counter)

# print ("heads total",heads_counter)
# print ("tails total",tails_counter)



# # User Object Generator
# users = []

# def create_user(name, age, username):
#   user = {
#     "name": name,
#     "age": age,
#     "username": username
#   }
#   return user

# count = 0
# while count < 3:
#   user = create_user(input("Name: "), input("Age: "), input("Username: "))
#   print(user)
#   users.append(user)
#   count+=1

# print(users)

# for user in users:
#   print(user)

# try:
#   number = int(input("Guess the Magic Number: "))
#   if number == 5:
#     print("That's the Magic Number")
#   print(number)
# except ValueError:
#   print("Invalid Input")

# # Number Guesser
# correct = False

# while correct == False:
#   try:
#     number = input("Guess the Magic Number: ")
#     if number == "exit":
#       correct = True
#       print("quitting...")
#     if number == "5":
#       print("That's the Magic Number")
#       correct = True
#     else:
#       print("It's not " + str(number))
#   except ValueError:
#     print("Invalid Input")


# # Opening and Reading Files
# file = open("/Users/ctavolazzi/Code/Harold/chatbot/node_modules/react-conditionally-render/LICENCE.txt", "r")
# print(file.readable())
# # print(file.read())
# for line in file.readlines():
#   print("line")

# file.close()

