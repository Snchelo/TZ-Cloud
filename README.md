## Порядок выполнения команд для запуска проекта:

# Переходим в папку со скриптом

Создать виртуальное окружение в папке venv.

``` bash
   python3 -m venv venv
```

Устанавливить все библиотеки из файла requirements.txt

```bash
   pip install -r requirements.txt 
```

Активировать окружение

```bash
  .venv\Scripts\activate 
```

Запустить файл с кодом Python

```bash
cd ./src/scripts    
python tz_python.py 
```

Запустить файл со скриптом Silenium

```bash
cd ./src/scripts    
python tz_selenium.py
```
