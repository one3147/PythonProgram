import bcrypt

def compare_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

hashed_password = b'$2a$10$/KQR/cN9K7.pslGxJnZAp.qW04GE/mgfmzLlQWc/XYsZvA2yKB.yu'

# User input
while(1):
    user_input = input("Enter the password: ")

    if compare_password(user_input, hashed_password):
        print("O")
    else:
        print("X")
