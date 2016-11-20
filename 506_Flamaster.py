import sys


def flamaster(n):
    wyraz = ""
    i = 0
    while i < len(n)-1:
        licznik = 1
        for j in range(i, len(n)-1):
            if  n[j] == n[j+1]:
                licznik += 1
            else:
                i = i + licznik
                break
        wyraz = wyraz + n[j] + str((lambda licznik: licznik if licznik > 2  else '')(licznik))
    return wyraz

t = int(sys.stdin.readline())
wynik = []
for i in range(t):
    wynik.append(flamaster(sys.stdin.readline()))

for i in wynik:
    sys.stdout.write(str(i) + "\n")

