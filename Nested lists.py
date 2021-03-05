if __name__ == '__main__':

    marks = [[input(),float(input())] for i in range(int(input()))]

    secondlarg = sorted(set([j for i,j in marks]))[1]
    
    #print(secondlarg)
    print("\n".join(sorted([i for i,j in marks if j==secondlarg])))