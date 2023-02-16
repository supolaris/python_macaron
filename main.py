if __name__ == '__main__':
    x = int(input("Input of x"))
    y = int(input("Input of y"))
    z = int(input("Input of z"))
    n = int(input("Input of n"))

    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))