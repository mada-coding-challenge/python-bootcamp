rangeNums = int(input("Enter number: "))

evenCount = 0
for number in range(rangeNums):
    if number % 2 == 0:
        print(f"{number} is even")
        evenCount += 1
    else:
        print(f"{number} is odd")

print(f"Total even numbers: {evenCount} And total is {rangeNums}")



