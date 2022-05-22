list = []
while(True):
    a = input("Введите число: ")
    print(type(a))
    if a != a.empty:
        list.append(a)
    else:
        break
    
print(min(list))
