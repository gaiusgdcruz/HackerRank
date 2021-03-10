def count_substring(string, sub_string):
    result = []
    for i in range(len(string)):
        if string.startswith(sub_string,i) == True:
            result.append(i)
    #print(result)
    count = len(result)
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)