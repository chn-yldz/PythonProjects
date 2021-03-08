#Caesar Cipher Algorithm
import time
def caesar():
    print("To do the encryption : 1\nTo decrypt : 2")
    choice = int(input("Your choice :"))
    if choice == 1:
        encryptedMessage = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        message = input("Message :")
        key = int(input("Key :"))
        for i in message.lower():
            if i not in alphabet:
                encryptedMessage+=i
            else:
                encryptedMessage += alphabet[(alphabet.index(i)+key) % len(alphabet)]
        print("Message Is Encrypted!!")
        time.sleep(2)
        print("Encrypted Message : {}".format(encryptedMessage))
    elif choice == 2:
        decryptedMessage = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        message = input("Message :")
        key = int(input("Key :"))
        for i in message.lower():
            if i not in alphabet:
                decryptedMessage += i
            else:
                decryptedMessage += alphabet[(alphabet.index(i)-key) % len(alphabet)]
        print("Message is Decrypted!!")
        time.sleep(2)
        print("Decrypted Message : {}".format(decryptedMessage))
    else:
        print("Wrong choice!!!")

