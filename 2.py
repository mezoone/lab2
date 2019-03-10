stroka = str(input("Введите строку: "))
m = stroka.split(' ')
for i in range (len(m)):
    if len(m[i])<10:
        print(m[i])
