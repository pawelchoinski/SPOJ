import sys

def czy_pierwsza(n):
    try:
        n = int(n)
    except ValueError:
        pass
    else:
        if n < 2:
            return "NIE \n"
        else:
            i = 2
            while i >= 2 and i * i <= n:
                if n % i == 0:
                    return "NIE \n"
                    break
                i += 1
            return "TAK \n"

t = int(sys.stdin.readline())

for i in range(t):
    sys.stdout.write(czy_pierwsza(int(sys.stdin.readline())))

