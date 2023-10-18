start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start % 2 == 0:
    start += 1  # Ensure the starting number is odd

print("Odd numbers between", start, "and", end, "are:")

for num in range(start, end + 1, 2):
    print(num)
