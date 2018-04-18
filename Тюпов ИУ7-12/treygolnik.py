#Тюпов Артем ИУ7-12
#Написать программу, которая определяет длины сторон треугольника
#Найти биссектрису, проведенную из наибольшего угла
#Определить является ли треугольник прямоугольным
#Ввести координаты точки и определить находиться ли точка внутри треугольника
#Если находиться, то найти расстояние от точки до ближайшей стороны треугольника
from math import sqrt,acos,cos,degrees,sin,radians
try:
    #Ввод вершин треугольника
    x1,y1=map(int,input('Введите координаты 1ой вершины треугольника x и y через пробел: ').split(' '))
    x2,y2=map(int,input('Введите координаты 2ой вершины треугольника x и y через пробел: ').split(' '))
    x3,y3=map(int,input('Введите координаты 3ой вершины треугольника x и y через пробел: ').split(' '))
    
    #Считаем длины
    leng1=float(sqrt((x2-x1)**2+(y2-y1)**2))
    leng2=float(sqrt((x3-x2)**2+(y3-y2)**2))
    leng3=float(sqrt((x1-x3)**2+(y1-y3)**2))
    
    #Считаем углы
    a1=degrees(acos((leng1**2+leng2**2-leng3**2)/(2*leng1*leng2)))
    a2=degrees(acos((leng2**2+leng3**2-leng1**2)/(2*leng2*leng3)))
    a3=degrees(acos((leng3**2+leng1**2-leng2**2)/(2*leng3*leng1)))
    if (leng1+leng2<leng3)or(leng2+leng3<leng1)or(leng3+leng1<leng2)or(a1==0)or(a2==0)or(a3==0):
        B=False
    else:
        B=True
    if (B==True):    
        #В зависимости от наибольшего угла считаем биссектрису
        if (a1>a2) and (a1>a3):
            ax=180-a2-a1/2
            biss=leng2*sin(radians(a2))/sin(radians(ax))
            print('Длина биссектрисы треугольника, исходящая из наибольшего угла: {:.5f}'.format(biss))
        if (a2>a1) and (a2>a3):
            ax=180-a3-a2/2
            biss=leng3*sin(radians(a3))/sin(radians(ax))
            print('Длина биссектрисы треугольника, исходящая из наибольшего угла: {:.5f}'.format(biss))
        if (a3>a2) and (a3>a1):
            ax=180-a1-a3/2
            biss=leng1*sin(radians(a1))/sin(radians(ax))
            print('Длина биссектрисы треугольника, исходящая из наибольшего угла: {:.5f}'.format(biss))
        #Определяем является ли треугольник прямоугольным
        if (a1>89.89)and(a1<91.0) or (a2>89.89)and(a2<91.0) or (a3>89.89)and(a3<91.0):
            print('Треугольник прямоугольный')
        else:
            print('Треугольник не прямоугольный')
            
        #Ввод точки O(x,y)
        x,y=map(int,input('Введите координаты точки x и y, для проверки ее принадлежности заданному треугольнику: ').split(' '))

        #Считаем периметры треугольников с вершиной O(x,y) и данного треугольника
        p=(leng1+leng2+leng3)/2
        p1=(leng1+sqrt((x-x1)**2+(y-y1)**2)+sqrt((x-x2)**2+(y-y2)**2))/2
        p2=(leng2+sqrt((x-x2)**2+(y-y2)**2)+sqrt((x-x3)**2+(y-y3)**2))/2
        p3=(leng3+sqrt((x-x3)**2+(y-y3)**2)+sqrt((x-x1)**2+(y-y1)**2))/2

        #Считаем площади треугольников с вершиной O(x,y) и данного треугольника
        S=sqrt(p*(p-leng1)*(p-leng2)*(p-leng3))     
        S1=sqrt(p1*(p1-leng1)*(p1-sqrt((x-x1)**2+(y-y1)**2))*(p1-sqrt((x-x2)**2+(y-y2)**2))) 
        S2=sqrt(p2*(p2-leng2)*(p2-sqrt((x-x2)**2+(y-y2)**2))*(p2-sqrt((x-x3)**2+(y-y3)**2)))
        S3=sqrt(p3*(p3-leng3)*(p3-sqrt((x-x3)**2+(y-y3)**2))*(p3-sqrt((x-x1)**2+(y-y1)**2)))

        #Определяем принадлежность точки
        if (S>=(S1+S2+S3)):
            print('Точка принадлежит заштрихованной области')
            a=True
        else:
            print('Точка не принадлежит заштрихованной области')
            a=False
            
        #Считаем длину наименьшего отрезка от точки O(x,y) до стороны треугольника
        a1=y2-y1
        a2=y3-y2
        a3=y1-y3
        b1=x1-x2
        b2=x2-x3
        b3=x3-x1
        c1=x1*(y1-y2) + y1*(x2-x1)
        c2=x2*(y2-y3) + y2*(x3-x2)
        c3=x3*(y3-y1) + y3*(x1-x3)    
        if a:
            if (y==(-a1*x-c1)/b1) or (y==(-a2*x-c2)/b2) or (y==(-a3*x-c3)/b3):
                print('Точка лежит на одной из сторон треугольника')
            else:
                h1=2*S1/leng1
                h2=2*S2/leng2
                h3=2*S3/leng3
                if (h1>h2) and (h1>h3): print('Расстояние от точки O до ближайшей стороны: {:.5f}'.format(h1))
                if (h2>h3) and (h2>h1): print('Расстояние от точки O до ближайшей стороны: {:.5f}'.format(h2))
                if (h3>h1) and (h3>h2): print('Расстояние от точки O до ближайшей стороны: {:.5f}'.format(h3))
                
    else:
        print('Треугольник не существует')
        
except ValueError:
    print('Вводите данные в виде: 3 2, где x=3, а y=2')
except ZeroDivisionError:
    print('Деление на ноль')    
        

