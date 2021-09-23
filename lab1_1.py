import math
print("ЛАБОРАТОРНА РОБОТА №1. ПРОГРАМУВАННЯ ЛІНІЙНИХ АЛГОРИТМІВ ТА  РОЗГАЛУЖЕНИХ ПРОЦЕСІВ")
print("Чемериський Максим, КМ-11, 27 варіант")
print("Знайти (в радіанах в градусах) всі кути трикутника зі сторонами а, b, с.")
print("")
while True:
    try:
        A = float(input("Введіть довжину сторони А у см: "))
    except ValueError:
        print("Значення некоректне, повторіть введення")
        continue
    else:  
        break
while True:
    try:
        B = float(input("Введіть довжину сторони B у см: "))
    except ValueError:
        print("Значення некоректне, повторіть введення")
        continue
    else:  
        break
while True:
    try:
        C = float(input("Введіть довжину сторони C у см: "))
    except ValueError:
        print("Значення некоректне, повторіть введення")
        continue
    else:  
        break
cosA = float((C**2 + B**2 - A**2) / (2*C*B))
cosB = float((C**2 + A**2 - B**2) / (2*C*A))
cosC = float((A**2 + B**2 - C**2) / (2*A*B))

angleArad = math.acos(cosA)
angleBrad = math.acos(cosB)
angleCrad = math.acos(cosC)

angleA = (180/math.pi) * angleArad
angleB = (180/math.pi) * angleBrad
angleC = (180/math.pi) * angleCrad

print("Кут А = " + str(round(angleA)) + " градус(ів) або " + str(round(angleArad,2)) +" радіан")
print("Кут В = " + str(round(angleB)) + " градус(ів) або " + str(round(angleBrad,2)) +" радіан")
print("Кут С = " + str(round(angleC)) + " градус(ів) або " + str(round(angleCrad,2)) +" радіан")
print("Дякую за використання програми, гарного дня!")