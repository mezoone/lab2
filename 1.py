my_number = 12
user_number = int(input("Введите число: "))
while user_number != my_number:
    print("Не верно")
    user_number = int(input("Введите число повторно: "))
print("Верно")
