# Template for P33

def main():
    number  = input()
    a, b , c = number
    a = int(a)
    b = int(b)
    c = int(c)
    sum = a**3 + b**3 + c**3
    number = int(number)
    if sum == number :
        print('Sum of Cubes is {}. It is the same as the number {}'.format(sum, number))
    else :
        print('Sum of Cubes is {}. It is NOT same as the number {}'.format(sum, number))    
if __name__ == "__main__":
    main()
