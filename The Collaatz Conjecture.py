
n = int(input("Insert a number:")) + 1

for i in range(1,n):
    print(i)
    while i != 1:
        if i % 2 == 0:
            i = i/2
            print(round(i))
        else:
            i = 3*i+1
            print(round(i))
    print('\n')