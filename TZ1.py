
def bubble_sort(numbers):
    # вводим пузырьковую сортировку
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def process_numbers():
    # получаем ввод от пользователя и разделяем его по пробелам
    input_str = input("Введите числа через пробел: ")
    
    # преобразуем строку в список чисел
    try:
        numbers = list(map(float, input_str.split()))
    except ValueError:
        print("Ошибка! Пожалуйста, вводите только числа.")
        return None, None, None, None
    
    # фильтруем чётные числа (делятся на 2 без остатка, исключая 0)
    even_numbers = [num for num in numbers if num % 2 == 0 and num != 0]
    
    # находим максимальное и минимальное число
    if numbers:
        max_num = max(numbers)
        min_num = min(numbers)
        sorted_numbers = bubble_sort(numbers.copy())  # cортируем копию списка
    else:
        max_num = min_num = sorted_numbers = None
    
    return even_numbers, max_num, min_num, sorted_numbers

print("Программа для обработки чисел")
even_numbers, maximum, minimum, sorted_nums = process_numbers()
    
if even_numbers is not None:
    if even_numbers:
        print("Чётные числа из введённых:", even_numbers) # однако, чтоб не было скобок можно расскрыть с помощью .join(map(str, even_numbers))
    else:
        print("Чётные числа не найдены.")
    
    if maximum is not None and minimum is not None:
        print(f"Максимальное число: {maximum}")
        print(f"Минимальное число: {minimum}")
    else:
        print("Список чисел пуст.")
    
    if sorted_nums:
        print("Отсортированный список:", sorted_nums) # тоже самое, чтоб не было скобок можно расскрыть с помощью .join(map(str, even_numbers))
    else:
        print("Нет чисел для сортировки.")
else:
    print("Не удалось обработать ввод.")