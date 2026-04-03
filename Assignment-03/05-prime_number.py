def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime Number"
    return "Prime Number"
n = int(input("Enter a number: "))
print( prime(n))