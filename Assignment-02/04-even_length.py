s = input("Enter string: ")
word = s.split()
for word in word:
    if len(word) % 2 == 0:
        print(word)