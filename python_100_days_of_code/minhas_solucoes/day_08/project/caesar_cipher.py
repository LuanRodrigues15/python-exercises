alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""  
    for letter in original_text:
        if letter in alphabet:
            position = (alphabet.index(letter) + shift_amount) % 26  # wrap-around
            cipher_text += alphabet[position]
        else:
            cipher_text += letter
    return cipher_text

if direction == "decode":
    shift *= -1

result = encrypt(text, shift)
print(f"The {direction}d text is: {result}")