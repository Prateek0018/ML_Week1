num = int(input("Enter a number: "))
count = 0
if num == 0:
    count = 1
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)
