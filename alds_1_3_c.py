class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None
    

class MyDLL:
    def __init__(self):
        # 番兵：仮想的な先頭
        self.sentinel = Node(None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
    
    def insert(self, x):
        # 連結リストの先頭にキー x を持つ要素を継ぎ足す。
        new = Node(x)
        new.next = self.sentinel.next # 新しく先頭.next = 番兵.next = 今まで先頭
        self.sentinel.next.prev = new # 番兵.next.prev = 今まで先頭.prev = 新しく先頭
        self.sentinel.next = new      # 番兵.next = 新しく先頭
        new.prev = self.sentinel      # 新しく先頭.prev = 番兵

    def listSearch(self, x):
        cursor = self.sentinel.next # 番兵の次の要素から巡る
        while (cursor != self.sentinel) & (cursor.key != x):
            cursor = cursor.next
        return cursor
    
    def deleteNode(self, node):
        # あるノードを削除するとき
        # 例 A - B - C でBを削除
        if node!=self.sentinel: # Bは番兵ではないことを確認
            node.prev.next = node.next # B.prev.next = A.next = B.next = C
            node.next.prev = node.prev # B.next.prev = C.prev = B.prev = A

    def deleteKey(self, x):
        self.deleteNode(self.listSearch(x))
        
    def deleteFirst(self):
        # リストの先頭の要素を削除する。
        self.deleteNode(self.sentinel.next)
        
    def deleteLast(self):
        # リストの末尾の要素を削除する。        
        self.deleteNode(self.sentinel.prev)
        
    def print(self):
        cursor = self.sentinel.next
        key_list = []
        while cursor != self.sentinel:
            key_list.append(cursor.key)
            cursor = cursor.next   
        print(' '.join(key_list))


def main():
    n = int(input())
    commands = (input() for i in range(n)) # generator式リスト内包表記
    dll = MyDLL()
    for c in commands:
        if 'insert' in c:
            dll.insert(c.split()[1])
        elif 'First' in c:
            dll.deleteFirst()
        elif 'Last' in c:
            dll.deleteLast()
        elif 'delete' in c:
            dll.deleteKey(c.split()[1])
        else:
            print("the command dont't exist")
            print(c)
    dll.print()

import time

if __name__=='__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print(elapsed)