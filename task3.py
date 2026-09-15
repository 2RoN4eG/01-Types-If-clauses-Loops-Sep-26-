"""
## Задача 3* — количество дней в месяце

Попросить пользователя ввести **название месяца на английском** и **номер года**.  
Вывести количество дней в этом месяце.

**Пример:**

- Дано: `February 2026`
- Результат: `28`

---
"""
month = input("input month: ")
year = int(input("input year: "))

match(month):
    case 'January':
        days = 31
    case 'February' if year % 4 == 0:
        days = 29
    case 'February':
        days = 28 
    case 'March':
        days = 31
    case 'April':
        days = 30
    case 'May':
        days = 31 
    case 'June':
        days = 30 
    case 'July':
        days = 31 
    case 'August':
        days = 31
    case 'September':
        days = 30
    case 'October':
        days = 31
    case 'November':
        days = 30
    case 'December':
        days = 31
    case _:
        print("Не правильно задан месяц: месяц должен быть на английском с большой буквы")

print("Результат: ", days)