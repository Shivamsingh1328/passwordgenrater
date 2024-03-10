#simple password generator 

import string
import random

 
def generate_password(lenght,use_special_charts=False):
    characters = string.ascii_letters + string.digits
    if use_special_charts:
        characters +=string.punctuation
        password = ''.join(random.choice(characters) for _ in range(lenght))
        return password




def main():
    print("Password Generator")
    try:
        lenght=int(input("Enter the desired password lenght:"))
        use_special_charts = input("Include special character? y/n:").lower()=='y'
        if lenght<=0:
            print("password lenght should be a positive number.")
        else:
            password = generate_password(lenght,use_special_charts)
            print("Your Generated Password=",password)

    except:
        print("Invalid Input")

if __name__=="__main__":
    main()
    