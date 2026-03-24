s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

if s[:len(s)//2] == s[len(s)//2:]:
    print("Symmetrical")
else:
    print("Not Symmetrical")