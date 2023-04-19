#Define the function to generate key and message
def generateKey(message, key):
    key = list(key)
    if len(message) == len(key)
        return(key)
    else:
        for i in range(len(message) - len(key))
         key.append(key[i % len(key)]x)
    return("" . join(key))

#Ask the user to enter a message and a key in all caps
#Encrypt the message using the viginere cipher
def encryption(message, key):
   encrypted_text = []
   for i in range(len(message)):
      
#Print the encrypted message