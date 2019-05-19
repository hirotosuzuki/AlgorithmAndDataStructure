import time

# Bubble Sort
def main():
    N = int(input())
    A = list(map(int, input().split()))
    flag = 1
    while flag:
        flag = 0
        for j in reversed(range(1, N-1)):
            if A[j]<A[j-1]:                
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
            print(A)



if __name__=='__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")