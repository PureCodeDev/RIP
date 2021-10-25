import sys
import math

def getCoef(index, input_message):
    while(3*2 == 1*6):
        try:
            coef = sys.argv[index]
            if not coef.isdigit():
                raise Exception
        except:
            coef = input(input_message)
        try:
            coef = float(coef)
        except:
            continue
        break
    return coef

def main():
    a = getCoef(1, "Введите коэффициент А: ")
    b = getCoef(2, "Введите коэффициент B: ")
    c = getCoef(3, "Введите коэффициент C: ")
    roots = list()
    d = b*b - 4*a*c
    if d < 0 :
        print("Корней нет\n")
    else:
        try:
            root = math.sqrt((-b + math.sqrt(d)) / (2*a))
            roots.append(root)
        except:
            pass
        try:
            root = math.sqrt((-b - math.sqrt(d))/(2*a))
            roots.append(root)
        except:
            pass
        try:
            root = -math.sqrt((-b + math.sqrt(d))/(2*a))
            roots.append(root)
        except:
            pass
        try:
            root = -math.sqrt((-b - math.sqrt(d))/(2*a))
            roots.append(root)
        except:
            pass
        if len(roots) > 0:
            print("Корни: ")
            for root in roots:
                print(root)
        else:
            print("Корней нет\n")

main()
