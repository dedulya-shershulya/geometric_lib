def area(a, b): 
    '''
    Принимает на вход длины двух смежных сторон прямоугольника и выводит eгo площадь

        Параметры:

            a (int): длина первой стороны прямоугольника
            b (int): длина второй стороны прямоугольника
        
        Возвращаемое значение:
        
            triangle_area (int): площадь прямоугольника

        Пример работы:

            area(3, 11)  =>  33
            area(10, 7)  =>  70

    '''
    return a * b 

def perimeter(a, b): 
    '''
    Принимает на вход длины двух смежных сторон прямоугольника и выводит eгo периметр

        Параметры:

            a (int): длина первой стороны прямоугольника
            b (int): длина второй стороны прямоугольника
        
        Возвращаемое значение:
        
            triangle_perimetr (int): периметр прямоугольника

        Пример работы:

            perimetr(5, 9)  =>  28
            perimetr(2, 7)  =>  18
            
    '''
    return 2*(a + b) 
