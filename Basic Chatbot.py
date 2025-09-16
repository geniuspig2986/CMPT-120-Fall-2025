import random
# Chatbot
# Author: Shenghua Jin
# September 8 2025

# === Algorithm ===
# Print out a greeting
print("Hello! I'm a Chatbot.")
# Get the user's name form input
print("What's your name?")
name = input()
# Cover edge cases
# Respond nicely
print("Nice to meet you " + name)

print("fav book?")
book = input()

comment_choices = ["nice book", "cool book", "bad book not cool"]
print(random.choice(comment_choices))

print("how are you today?")
reply = input()
if reply == "good":
    print("thats nice")
elif reply == "bad":
    print("oh no")
else:
    print("cool")

