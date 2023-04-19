#This will generate a key and will return the keyword if it is the same length with the message
def generateKey(message, key): 
  key = list(key) 
  if len(message) == len(key): 
    return(key) 
  else: 
    for i in range(len(message) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 

#This part of the code handles how to encrypt the message inputted
def encryption(message, key):
    encrypted_text = []
    for i in range(len(message)):
        number_equivalent = (ord(message[i]) +ord(key[i])) % 26
        number_equivalent += ord('A')
        encrypted_text.append(chr(number_equivalent))
    return("" . join(encrypted_text))

#This part will ask the user to input their message, keyword, and finally prints the encrypted message using vigenere code
if __name__ == "__main__": 
    message = input("Input a message you want to encrypt(in all caps):")
    keyword = input("Please input a keyword to encrypt the message(in all caps):")
    key = generateKey(message,keyword)
    encrypted_message = encryption(message, key)
    print("Message is", message)
    print("Encrypted message is", encrypted_message)