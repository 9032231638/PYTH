# print(5, 9, 4)

# # Задача 2: Найдите сумму цифр трехзначного числа.

d = int(input("Введите трехзначное число: "))
print(d // 100 + (d // 10) % 10 + d % 10)
