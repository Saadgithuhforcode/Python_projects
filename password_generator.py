import random
import string

def password_new(length):
    # ascii is a value system of sorts ig ..
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    pwd = password_new(length=6)
    print(f"the password is: {pwd}")
