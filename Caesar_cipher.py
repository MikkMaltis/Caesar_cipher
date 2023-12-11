chars = ['a','b','c','d', 'e','f','g','h','i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

text = input("Enter the text: ")
key = int(input("Enter the key: "))
result = []

for char in list(text):
    if char in chars:
        print(chars[(chars.index(char) + key) % len(chars)])
    else:
        result.append(char)

    print(result)