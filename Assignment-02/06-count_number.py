s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")
count = 0
for i in s1:
    if i in s2:
        count += 1
print("Match Characters: ", count)