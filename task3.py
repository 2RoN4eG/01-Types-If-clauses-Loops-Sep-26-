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

days = None
match(month):
    case 'January' | 'january':
        days = 31
    case 'February' | 'february' if year % 4 == 0:
        days = 29
    case 'February' | 'february':
        days = 28 
    case 'March' | 'march':
        days = 31
    case 'April' | 'april':
        days = 30
    case 'May' | 'may':
        days = 31 
    case 'June' | 'june':
        days = 30 
    case 'July' | 'july':
        days = 31 
    case 'August' | 'august':
        days = 31
    case 'September' | 'september':
        days = 30
    case 'October' | 'october':
        days = 31
    case 'November' | 'november':
        days = 30
    case 'December' | 'december':
        days = 31
    case _:
        print("Не правильно задан месяц: месяц должен быть на английском")

print("Результат: ", days)
