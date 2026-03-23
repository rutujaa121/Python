n = int(input("Enter a Number: "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if n == sum: 
    print(n, "Armstrong Number")
else:
    print(n, "Not Armstrong Number")