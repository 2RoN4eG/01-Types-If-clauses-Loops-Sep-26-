"""
## Задача 3* — количество дней в месяце

Попросить пользователя ввести **название месяца на английском** и **номер года**.  
Вывести количество дней в этом месяце.

**Пример:**

- Дано: `February 2026`
- Результат: `28`

---
"""


# month = input("input month: ")
# year = int(input("input year: "))

def get_days(month, year):
    match(month.lower()):
        case 'January' | 'january':
            return 31
        case 'February' | 'february' if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
            return 29
        case 'February' | 'february':
            return 28 
        case 'March' | 'march':
            return 31
        case 'April' | 'april':
            return 30
        case 'May' | 'may':
            return 31 
        case 'June' | 'june':
            return 30 
        case 'July' | 'july':
            return 31 
        case 'August' | 'august':
            return 31
        case 'September' | 'september':
            return 30
        case 'October' | 'october':
            return 31
        case 'November' | 'november':
            return 30
        case 'December' | 'december':
            return 31
        case _:
            raise Exception("Не правильно задан месяц: месяц должен быть на английском")


if __name__ == "__main__":
    days = get_days("February", 2000)
    print("Результат: ", days)

    days = get_days("February", 2004)
    print("Результат: ", days)

    days = get_days("February", 2100)
    print("Результат: ", days)

    days = get_days("February", 1900)
    print("Результат: ", days)
