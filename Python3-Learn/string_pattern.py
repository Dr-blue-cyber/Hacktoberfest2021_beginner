n = int(input("Enter the number of rows : "))

ch = 64

for i in range(1, n+1):
    for j in range(1, i+1):
        print("{0}".format(chr(ch+j)), end=" ")
    print()

for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        print("{0}".format(chr(ch+j)), end=" ")
    print()

