from math import pow

if __name__ == "__main__":
    try:
        x =float(input("Введите значение x: "))
    except ValueError:
        print("Введите число, а не строку")
        x =float(input("Введите значение x: "))
    y1 = (pow(pow(x,4)+pow(x,3)-x*x-x+1,1/3))
    y2 = (pow(x,4)+2*pow(x,3)-2*x+1)
    try:
        y3 = y1/y2
    except ZeroDivisionError:
        print("Деление на ноль!")
    print("Полученное значение: ",y3)
    input("Для завершения работы нажмите Enter")    
        
    
    
