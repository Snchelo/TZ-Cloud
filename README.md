## Порядок выполнения команд для запуска проекта:

Создать виртуальное окружение в папке venv.

``` bash
   python3 -m venv venv
```

Активировать окружение

```bash
  .venv\Scripts\activate 
```

Устанавливить все библиотеки из файла requirements.txt

```bash
   pip install -r requirements.txt 
``` 

Запуск программы связанной с числами 

```bash
numbers = list(map(float, input("Введите список чисел через пробел: ").split()))

print("Четные числа:")
for num in numbers:
    if num % 2 == 0 and num != 0:
        print(num, end=" ")
print()

if not numbers:
    print("Список пуст")
else:
    max_num = min_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num: max_num = num
        if num < min_num: min_num = num
    print(f"Максимальное: {max_num}\nМинимальное: {min_num}")

n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Список в порядке возрастания:", numbers)
```

Запуск скрипта с помощью Selenium

```bash
from selenium import (webdriver)
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://example.com")

assert "Example" in driver.title, "Заголовок не содержит 'Example'"

more_info_link = driver.find_element("css selector", "a[href*='iana.org']")
more_info_link.click()

assert driver.current_url == "https://www.iana.org/help/example-domains", "URL не совпадает!"
```

