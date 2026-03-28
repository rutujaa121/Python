s = input("Enter String: ").lower()
if all(v in s for v in "aeiou"):
    print("Accepted")
else:
    print("Not Accepted")