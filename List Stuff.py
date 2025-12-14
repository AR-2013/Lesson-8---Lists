listy = [1, 4, 6, 2, 7, 3, 8, 0, 5, 9]
count = 0

for i in listy:
    count += i

avg = count/len(listy)

print("Sum =", count)
print("Average =", avg)

listy.sort

print("Smallest element is", listy[0])
print("Largest element is", listy[-1])