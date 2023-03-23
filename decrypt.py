#Cryptography Challenge #1

import random, time

#A basic encryption algorithm...
def decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    current_index = 0
    plaintext = ciphertext[current_index]
    current_index = current_index + key + 1
    while current_index < len(ciphertext):
      plaintext += ciphertext[current_index]
      current_index = current_index + key + 1
      
    return ciphertext
 
 
#Main program starts here...

#Input...
ciphertext = input("Enter a message to decrypt (ciphertext)")
key = int(input("Input a key as a number between 1 and 10"))

while not (key>=1 and key<=10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))

#Process... 
print("...")
time.sleep(1)

print("Decrypting ciphertext...")
time.sleep(1)

print("...")
time.sleep(1)

plaintext = decrypt(ciphertext, key)

#Output...
print("Plaintext:")
print(plaintext)
