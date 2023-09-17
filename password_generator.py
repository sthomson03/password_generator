# import "random" module to generate random chars & symbols for the password
import random

# import "bcrypt" module to salt and hash generated password before storing
import bcrypt

# creating a constant "MAX_LENGTH" to store the max length of the generated password
MIN_LENGTH = 6
MAX_LENGTH = 30
CHARACTER_POOL_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
CHARACTER_POOL_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHARACTER_POOL_SYMBOLS = "!@£$%^&*"
CHARACTER_POOL_NUMBERS = "0123456789"

def yes_no_validation(prompt):
    while True:
        response = input(prompt + " (y/n): ")
        if response.lower() == "y":
            return True
        elif response.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def get_password_requirements():
    while True:
        # ask user what length of password they want
        pass_length = input("Please enter the length of your password: \n")
        
        # input validation
        if pass_length.isdigit():
            pass_length = int(pass_length)
            
            if MIN_LENGTH <= pass_length <= MAX_LENGTH:
                break
            else:
                print("Your password must be between " + str(MIN_LENGTH) + " and " + str(MAX_LENGTH) + "!");
                continue
        else:
            print("Please enter a number to indicate the length of your password\n")
            continue
    
    pass_has_symbols = yes_no_validation("\nWould you like to use symbols in your password?")
    pass_has_uppercase = yes_no_validation("Would you like a combination of upper and lower case characters?")
    pass_has_numbers = yes_no_validation("Would you like numbers in your password?")
        
    return pass_length, pass_has_symbols, pass_has_uppercase, pass_has_numbers

def generate_password(pass_length, pass_has_symbols, pass_has_uppercase, pass_has_numbers):
    character_pool = CHARACTER_POOL_LOWERCASE
    
    required_characters = []

    if pass_has_symbols:
        required_characters.append(random.choice(CHARACTER_POOL_SYMBOLS))
        character_pool += CHARACTER_POOL_SYMBOLS
    if pass_has_uppercase:
        required_characters.append(random.choice(CHARACTER_POOL_UPPERCASE))
        character_pool += CHARACTER_POOL_UPPERCASE
    if pass_has_numbers:
        required_characters.append(random.choice(CHARACTER_POOL_NUMBERS))
        character_pool += CHARACTER_POOL_NUMBERS

    remaining_length = pass_length - len(required_characters)
    generated_password = ''.join(random.choice(character_pool) for _ in range(remaining_length))
    
    return ''.join(required_characters + list(generated_password))

# function to display the welcome message in console
def main():
    print("Password generator")
    print("Press \"enter\" to generate your password")
    
    file = open("password.txt", "x")
        
    while True:
        if input()=="":
            pass_length, pass_has_symbols, pass_has_uppercase, pass_has_numbers = get_password_requirements()
            generated_password = generate_password(pass_length, pass_has_symbols, pass_has_uppercase, pass_has_numbers)
            print("Your generated password is: " + generated_password)
            file = open("password.txt", "w")
            file.write(generated_password)
            file.close()
            break
    
main()