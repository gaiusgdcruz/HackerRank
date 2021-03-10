def solve(s):
    n = s.title()
    for i in range(len(n-1)):
        if n[i].isdigit:
            continue
            i += 2
            n[i].toupper

    return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
