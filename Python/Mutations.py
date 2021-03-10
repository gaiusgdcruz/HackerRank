def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    st = ''
    for i in l:
        st += i
    return st


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
