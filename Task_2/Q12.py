num = int(input("Enter a number: "))
original = num
power = len(str(num))  # Count digits
result = 0

while num > 0:
    digit = num % 10
    result += digit ** power
    num //= 10

if result == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
