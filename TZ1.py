
numbers = list(map(float, input("Введите список чисел через пробел: ").split()))

print("Четные числа:")
for num in numbers:
    if num % 2 == 0 and num != 0:
        print(num, end=' ')
print()

if numbers:
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f"Максимальное число: {max_num}")
    print(f"Минимальное число: {min_num}")
else:
    print("Список пуст")

n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Список в порядке возрастания:", numbers)
