def encrypt(text_value ,shift_value):
    encrypted_text =""
    for i in text_value:
        index_num = alphabet.index(i)
        new_index = index_num + shift_value
        encrypted_text += alphabet[new_index]
    return encrypted_text

def decrypt(text_value,shift_value):
    decrypted_text =""
    for i in text_value:
        index_num = alphabet.index(i)
        new_index = index_num - shift_value
        decrypted_text += alphabet[new_index]
    return decrypted_text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encrypt":
    print(f"the encrypted cipher text for the plain text is {encrypt(text,shift)}")
else:
    print(f"The decrypted plain tesxt for the cipher text is {decrypt(text,shift)}")