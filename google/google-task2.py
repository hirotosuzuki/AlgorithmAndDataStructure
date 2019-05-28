import time

def load_tree():
    # 改行
    _ = input()
    # number of nodes
    N = int(input())
    # edges
    edges=[list(map(int,input().split())) for i in range(N-1)]
    return N, edges

def bfs(X, N, edges):
    """
    K: 対象となるノード番号
    N: ノード数
    edges: エッジリスト
    dish: あるノードXから最も遠いノードまでの距離d(X)
    """
    K = X - 1
    roots=[ [] for i in range(N)]
    for a,b in edges:
        roots[a-1]+=[(b-1,1)]
        roots[b-1]+=[(a-1,1)]
    dist=[-1]*N
    stack=[]
    stack.append(K)
    dist[K]=0
    while stack:
        label=stack.pop(-1)
        for i,c in roots[label]:
            if dist[i]==-1:
                dist[i]=dist[label]+c
                stack+=[i]
    return max(dist)

def main():
    # number of test case
    C = int(input())
    for c in range(C):
        N, edges = load_tree()
        d_list = []
        for K in range(N):
            X = K + 1
            d_list.append(bfs(X, N, edges))        
        answer = min(d_list)
        print("Case #{case}: {answer}".format(case=c+1, answer=answer))

    


if __name__=='__main__':    
    main()