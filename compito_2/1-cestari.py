# exercise 
# import chiper modules:
from Crypto.Cipher import DES3, AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


# import of other modules 
import lec2
import sys 
import getpass
import os
def generate_key():
    pass

def encrypt_file():
    pass

def decrypt_file():
    pass

def main():
    menu_text = (
    "Choose an operation:\n"
    "1. Encrypt file (3DES)\n"
    "2. Decrypt file (3DES)\n"
    "3. Encrypt file (AES)\n"
    "4. Decrypt file (AES)\n"
    "5. Exit\n"
    )
    while True:
        # Prompt the user to choose an operation
        print(menu_text)
        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            # Encrypt file (3DES) operation
            algorithm = DES3
            operation = "encrypting"

            # Prompt the user for the input and output file paths
            in_file = input("Enter the path of the input file: ")
            out_file = input("Enter the path of the output file: ")

            # Prompt the user to choose whether to include message authentication
            authenticate = input("Include message authentication? (y/n) ").lower() == "y"

            # Generate a new key for encryption
            key = generate_key(algorithm)

            # Encrypt the input file and save the encrypted data to the output file
            encrypt_file(algorithm, key, in_file, out_file, authenticate)

            # Prompt the user to save the key to a file
            key_file = input("Enter a name for the key file: ")
            lec2.write_file(key_file)
            # with open(key_file, "wb") as f:
            #     f.write(key)

            print(f"File {operation}ed and key saved to {out_file} and {key_file}, respectively.")

        elif choice == 2:
            # Decrypt file (3DES) operation
            algorithm = DES3
            operation = "decrypting"

            # Prompt the user for the input and output file paths
            in_file = input("Enter the path of the input file: ")
            out_file = input("Enter the path of the output file: ")

            # Prompt the user to enter the key file path
            key_file = input("Enter the path of the key file: ")
            # Read the key from the specified file
            key = lec2.read_file(key_file)
            # with open(key_file, "rb") as f:
            #     key = f.read()
             # Prompt the user to choose whether the input file includes message authentication
            authenticate = input("Does the input file include message authentication? (y/n) ").lower() == "y"

            # Decrypt the input file and save the decrypted data to the output file
            decrypt_file(algorithm, key, in_file, out_file, authenticate)

            print(f"File {operation}ed and saved to {out_file}.")

        elif choice == 3:
            # Encrypt file (AES) operation
            algorithm = AES
            operation = "encrypting"

            # Prompt the user for the input and output file paths
            in_file = input("Enter the path of the input file: ")
            out_file = input("Enter the path of the output file: ")

            # Prompt the user to choose whether to include message authentication
            authenticate = input("Include message authentication? (y/n) ").lower() == "y"

            # Generate a new key for encryption
            key = generate_key(algorithm)

            # Encrypt the input file and save the encrypted data to the output file
            encrypt_file(algorithm, key, in_file, out_file, authenticate)

            # Prompt the user to save the key to a file
            key_file = input("Enter a name for the key file: ")
            # Read the key from the specified file
            key = lec2.read_file(key_file)
            # with open(key_file, "wb") as f:
            #     f.write(key)

            print(f"File {operation}ed and key saved to {out_file} and {key_file}, respectively.")

        elif choice == 4:
            # Decrypt file (AES) operation
            algorithm = AES
            operation = "decrypting"

            # Prompt the user for the input and output file paths
            in_file = input("Enter the path of the input file: ")
            out_file = input("Enter the path of the output file: ")

            # Prompt the user to enter the key file path
            key_file = input("Enter the path of the key file: ")
            # Read the key from the specified file
            key = lec2.read_file(key_file)
            # with open(key_file, "rb") as f:
            #      key = f.read()

            # Prompt the user to choose whether the input file includes message authentication
            authenticate = input("Does the input file include message authentication? (y/n) ").lower() == "y"

            # Decrypt the input file and save the decrypted data to the output file
            decrypt_file(algorithm, key, in_file, out_file, authenticate)

            print(f"File {operation}ed and saved to {out_file}.")

        elif choice == 5:
            # Exit operation
            print("Exiting...")
            sys.exit()
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

# Main function executing
if __name__ == "__main__":
    main()
