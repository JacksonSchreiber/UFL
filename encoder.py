#Jackson Schreiber

def encode(password):
    encoded_pass = ""
    for i in password: #iterate through each password digit
        if int(i) < 7:
            encoded_pass += str(int(i) + 3)
        else:
            encoded_pass += str(int(i) - 7)

    return encoded_pass

def decode(password):
    return "test"

def main():
    while(True):
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")


        choice = input("Please enter an option: ") #Menu selection stored

        if choice == "1": #Encoder function
            plain_pass = input("Please enter your password to encode: ")
            if len(plain_pass) != 8: #Check if password is 8 digits
                print("The password must be 8 digits.")
                plain_pass = ""
            else:
                encoded_pass = encode(plain_pass) #Encode the password, store it in encoded_pass variable
                plain_pass = "" #impenetrable 1337 security
                print("Your password has been encoded and stored!")

        elif choice == "2": #Uses decoder function
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}')

        elif choice == "3": #Quit
            exit()
main()
