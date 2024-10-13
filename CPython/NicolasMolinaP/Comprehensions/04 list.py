numbers = []
for i in range(1, 11):
    if i % 2 == 0:
     numbers.append(i * 2)

    print(numbers)
    
 #forma list comprehension
numbers_v2 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v2)