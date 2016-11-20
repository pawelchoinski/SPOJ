import sys

def ostania_cyfra_potegi(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        pass
    else:
        if b % 4 == 0:
            return a**4%10
        else:
            return a**(b%4)%10


t = int(sys.stdin.readline())
wynik=[]
for i in range(t):
    try:
        a, b = sys.stdin.readline().split(' ',1)
    except ValueError:
        pass
    else:
        wynik.append(ostania_cyfra_potegi(a, b))

for i in wynik:
    sys.stdout.write(str(i)+"\n")

