chars = ['a','b','c','d', 'e','f','g','h','i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

# encrypting
text = input("Enter the text: ")
key = int(input("Enter the key: "))
result = []

for char in list(text):
    if char in chars:
        print(chars[(chars.index(char) + key) % len(chars)])
    else:
        result.append(char)

    print(result)

# decrypting
text = input("Enter the text: ")
key = int(input("Enter the key: "))
result = []

for char in list(text):
    if char in chars:
        decrypted_char = chars[(chars.index(char) - key) % len(chars)]
        result.append(decrypted_char)
    else:
        result.append(char)

decrypted_text = ''.join(result)
print("Decrypted text:", decrypted_text)