# More Pythin experiments

# Asking user for their name in all caps
user_name = input('What is your name: ')
capped_user_name = user_name.upper()
# gets number length of capped_user_name
num_of_letters = len(capped_user_name)

#saying hello using text interpolation
print(f'Hello {capped_user_name}!)

# Tells them how many letters are in their name
print(f'YOUR NAME HAS {num_of_letters} LETTERS IN IT! AWESOME!')