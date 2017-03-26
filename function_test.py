import math
def rectangle_perimeter():
    length = int(raw_input('enter your length'))
    breath = int(raw_input('enter your breath'))
    ans = (length + breath) * 2
    print ans

while True :
    print ('1.an primeter')
    print ('2.an arae')
    print ('3.exit')
    ch=int(raw_input('enter your choice'))
    if ch==1:
        print '1.perimeter of rectangle'
        print '2.perimeter of circle'
        print '3.perimeter of square'
        print '4.perimter of triangle'
        n=int(raw_input('enter your choice'))
        if n==1:
            rectangle_perimeter()
        elif n==2:
            radius=int(raw_input('enter your radius'))
            ans =2*math.pi*radius
            print ans
        elif n==3:
            side =int(raw_input('enter your length'))
            ans=4*side
            print ans
        elif n==4:
            side1=int(raw_input('enter your side 1'))
            side2 = int(raw_input('enter your side 2'))
            side3 = int(raw_input('enter your side 3'))
            ans=side1+side2+side3
            print ans
    elif ch==2:
        print 'area of rectangle'
        print'area of circle'
        print'area of square'
        z=int(raw_input('enter your choice'))
        if z==1:
            length =int(raw_input('enter your length'))
            breath=int(raw_input('enter your breath'))
            ans=length*breath
            print ans
        elif z==2:
            radius=int(raw_input('enter your radius'))
            ans=2*math.pi*radius
            print ans
        elif z==3:
            side=int(raw_input('enter yur side'))
            ans=side*side
            print ans
    elif ch==3:
        break












