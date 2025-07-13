def encrypter(text, shift):
    encrypted_text =""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char)- 65+shift)%26+65)
        elif char.islower():
            encrypted_text += chr((ord(char)-97+shift)%26+97)
        else:
            encrypted_text+=char

    return encrypted_text

phrase = input("Enter sentence to encrypt: ")
shift = int(input("Enter shift value: "))
print(encrypter(phrase,shift))