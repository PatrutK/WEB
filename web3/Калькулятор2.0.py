import sys

sum, count = 0, 1
if len(sys.argv) < 2:
    print('NO PARAMS')
else:
    a = [i for i in sys.argv]
    try:
        for argv in sys.argv:
            if argv.isdigit():
                if count % 2 == 0:
                    sum -= argv
                    count += 1
                else:
                    # sum += argv
                    count += 1
    except ValueError:
        print('ValueError')
    print(sum)
