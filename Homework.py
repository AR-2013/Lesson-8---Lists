highest = int(input("Enter the lowest number in the range: "))
lowest = int(input("Enter the highest number in the range: "))

numbers = []
for num in range(highest, lowest + 1):
    numbers.append(num)

squared_numbers = []
for num in numbers:
    squared_numbers.append(num * num)

even_squares = []
odd_squares = []

for num in squared_numbers:
    if num % 2 == 0:
        even_squares.append(num)
    else:
        odd_squares.append(num)

print("Numbers in range:", numbers)
print("Squared numbers:", squared_numbers)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
