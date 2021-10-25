from lab_oop.rectangle import Rectangle
from lab_oop.circle import Circle
from lab_oop.square import Square

#import arrow

def main():
    r = Rectangle("синего", 2,2)
    c = Circle("красного",2)
    s = Square("желтого",2)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
