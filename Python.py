#Shenghua Jin
#Variables can overwrite functions

#print = 5;
#print ("hello world")
# will be an error
import random

print("fav book?")
book = input()

comment_choices = ["nice book", "cool book", "bad book not cool"]
print(random.choice(comment_choices))