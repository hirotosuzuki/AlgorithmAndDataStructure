import time

def main():
    # 第一行目の入力
    n = int(input())
    # 第２行目以降の入力
    r_list = [int(input()) for i in range(n)]
    score = -2000000000000000000000
    minv = r_list[0]
    """
    ループ内で
    今まで出た最小値を持っておく
    新しい値との差をとる
    既存のスコアより大きければスコアを更新
    """
    for r in r_list[1:]:# ここの開始位置を0番目からにしてしまうとscore<0の時もscore=0になってしまう
        score = max(score, r - minv) 
        minv = min(minv, r)        
    print(score)
    return score

if __name__=='__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

