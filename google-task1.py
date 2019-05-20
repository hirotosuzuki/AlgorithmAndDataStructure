import itertools


def load_tree():
    # 改行
    _ = input()
    # approximate price
    X = int(input())
    # number of flavors
    N = int(input())
    # flavors
    flavors = [int(input().split()[1]) for i in range(N)]
    # number of options
    M = int(input())
    if M!=0:
        options = [int(input().split()[1]) for i in range(M)]
    else:
        options = []
    # print(flavors)
    # print(options)
    return X, N, flavors, M, options


def main():
    # number of test case
    C = int(input())
    min_cost = 1000000000000
    for c in range(C):
        X, N, flavors, M, options = load_tree()
        for f in flavors:
            if len(options)==0:
                answer = f
            elif len(options)==1:
                if f >= X:
                    answer = f
                else:                     
                    min_cost = min(abs(X-f), abs(X-f-options[0]))
                    answer = X + min_cost
            else:
                if f >= X:
                    answer = f
                else:
                    c_1 = [abs(o + f - X) for o in options]
                    c_2 = [abs(a + b + f - X) for a, b in itertools.combinations(options, 2)]
                    min_cost = min(min(c_1), min(c_2))
                    answer = min_cost + X
        print("Case #{case}: {answer}".format(case=c+1, answer=answer))

    


if __name__=='__main__':    
    main()