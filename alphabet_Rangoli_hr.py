def print_rangoli(size):
    width=(2*(size-1))+(2*(size-1))+1
    size1=96+size  
    for i in range(size):   
        c=chr(size1)   
        for j in range(i):
            size1-=1
            c=c+chr(size1)
        for k in range(i):
            size1+=1
            c=c+chr(size1)
        size1=96+size
        c='-'.join(c)
        c=c.center(width,'-')
        print(c)
    for i in range(size-2,-1,-1):
        c=chr(size1)
        for j in range(i):
            size1-=1
            c=c+chr(size1)
        for k in range(i):
            size1+=1
            c=c+chr(size1)
        size1=96+size
        c='-'.join(c)
        c=c.center(width,'-')
        print(c)    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)