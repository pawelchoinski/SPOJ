import sys

html = ""
while True:
    start = 0
    end = 0
    try:
        linia = str(sys.stdin.readline())
    except ValueError:
        break
    except EOFError:
        break
    else:
        start = linia.find('<')
        end = linia.find('>')
        sys.stdout.write(str(start) + "\n")

# for i in suma:
#     sys.stdout.write(str(i)+"\n")
