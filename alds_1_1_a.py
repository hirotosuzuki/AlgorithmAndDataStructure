import time

# Insertion Sort
def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(' '.join([str(a) for a in A]))
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while (j>=0) and (A[j]>v):
            A[j+1] = A[j]
            j -= 1                            
        A[j+1] = v
        print(' '.join([str(a) for a in A]))            


if __name__=='__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")