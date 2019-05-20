import time

def BubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0
        for j in reversed(range(1, N)):
            if A[j]['value']<A[j-1]['value']:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
    return A

def SelectionSort(A, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j]['value']<A[minj]['value']:
                minj = j
        if i!=minj:
            A[i], A[minj] = A[minj], A[i]
    return A

def IsStable(answer, target):
    N = len(answer)
    for i in range(N):
        if answer[i]['value'] != target[i]['value']:
            return False
    return True

# Stable Sort
def main():
    N = int(input())
    A = tuple(
        map(lambda x: {'body': x, 'value': int(x[1])}, input().split())
    )
    print(A)
    bubble = BubbleSort(A, N)
    print(A)
    selection = SelectionSort(A, N)
    print(A)
    print(' '.join(map(lambda x: x['body'],bubble)))
    print('Stable')
    print(' '.join(map(lambda x: x['body'], selection)))
    if IsStable(bubble, selection):
        print('Stable')
    else:
        print('Not stable') 
    


if __name__=='__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")