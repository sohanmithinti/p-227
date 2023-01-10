print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encryption")
    msg = input("enter your message")
    key = int(input("enter key(1-94):"))

    encrypted_text = " "
    for i in range(len(msg)): 
        temp = (ord(msg[i]) + key)
        if(temp>126): 
            temp = temp-127 + 32

        encrypted_text += chr(temp)

    print("encrypted: " + encrypted_text)    

    main()


def decryption():
    print("decription")
    print("message can only be lower or upper case values")
    encrypt_message = input("enter encrypted text")
    decrypt_key = int(input("enter key(1-94): "))
    decrypted_text = " "
    for i in range(len(encrypt_message)):
        temp = (ord(encrypt_message[i]) - decrypt_key)
        if(temp<32):
            temp = temp+127 - 32

        decrypted_text += chr(temp)

    print("decrypted text: " + decrypted_text)        

   
if __name__ == "__main__":
    main()
