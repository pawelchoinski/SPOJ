import sys


suma = []
x = 0
while True:
    try:
        liczba = int(sys.stdin.readline())
    except ValueError:
        #sys.stdout.write(str(suma))
        break
    except EOFError:
        break
    else:
        x += liczba
        suma.append(x)

for i in suma:
    sys.stdout.write(str(i)+"\n")
