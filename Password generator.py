import random
import string

def password_generator(n):
    l_c=string.ascii_lowercase
    U_c=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation

    all_chars=l_c +U_c+digits+symbols
    password_chars = []
    if n >= 4: # Need at least 4 characters to guarantee one of each type
        password_chars.append(random.choice(l_c))
        password_chars.append(random.choice(U_c))
        password_chars.append(random.choice(digits))
        password_chars.append(random.choice(symbols))
        # Fill the rest of the password with random characters from all sets
        for _ in range(n-4):
            password_chars.append(random.choice(all_chars))
    else:
        for _ in range(n):
            password_chars.append(random.choice(all_chars))
        
    random.shuffle(password_chars)

    password = "".join(password_chars)
    return password

while True:
    try:
        n=int(input("Enter the desired length (e.g:12) :\n "))
        if n<=3:
            print("Enter a number more than 3")
        else:
            break
    except:
        print("Invalid input")
    
password_generated=password_generator(n)
print(f"The generated password of length {n} \n is {password_generated}")