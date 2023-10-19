from src.authentication.signup import SignUp
from src.app import main

if __name__ == '__main__':

    n = input("Press \n1 to login \n2 to signup \n")
    if n == '1':
        main()
    elif n == '2':
        SignUp().UserCreate()
        print("Login to your account")
        main()
    else:
        print("Invalid input")
        exit()

