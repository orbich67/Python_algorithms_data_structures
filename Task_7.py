a = int(input("Сторона a = "))
b = int(input("Сторона b = "))
c = int(input("Сторона c = "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник с такими сторонами не существует!")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")
