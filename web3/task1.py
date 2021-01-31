import sys

if len(sys.argv) < 3 or sys.argv[1].isalpha() or sys.argv[2].isalpha():
    print(0)
else:
    print(int(sys.argv[1]) + int(sys.argv[2]))
