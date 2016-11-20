import sys

n = int(sys.stdin.readline())
powierzchnia=[]
for i in range(n):
    powierzchnia.append(int(sys.stdin.readline())**2)

for a in powierzchnia:
    sys.stdout.write(str(a)+"\n")
