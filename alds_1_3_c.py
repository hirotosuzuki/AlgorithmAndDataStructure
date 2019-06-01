import time

class Node:
    def __init__(self, key, prev, next):
        self.key = key
        self.prev = prev
        self.next = next
    

class MyDLL:
    def __init__(self):
        self.linkedlist = []
        self.length = 0
    
    def isEmpty(self):
        if self.length==0:
            return True
        return False
    
    def insert(self, x):
        # 連結リストの先頭にキー x を持つ要素を継ぎ足す。
        if self.isEmpty():
            # 連結リストが空の時
            new = Node(x, None, None)            
        else:
            # 連結リストが空ではない時
            old = self.linkedlist[0] # 今まで先頭にいたノード
            new = Node(x, None, old) # 新しく先頭になるノード
            old.prev = new           # 今まで先頭にいたノードの前に新しいノードを登録
        self.linkedlist.insert(0, new)
        self.length += 1 # 連結リストの長さを更新

    def delete(self, x):
        # キー x を持つ最初の要素を連結リストから削除する。そのような要素が存在しない場合は何もしない。
        for node in self.linkedlist:
            if node.key==x:# キー x を持つ最初の要素    
                if node.prev is None:# 先頭だった時
                    node.next.prev = None # 次の要素の前の要素をNoneにする
                elif node.next is None:# 最後尾だった時
                    node.prev.next = None
                else:# 途中だった時
                    prev_node = node.prev
                    next_node = node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                self.linkedlist.remove(node)# listから削除 
                self.length -= 1     
                break # キーxを持つ最初だけで良いのでbreak
        
    def deleteFirst(self):
        # リストの先頭の要素を削除する。
        if not self.isEmpty():
            first = self.linkedlist.pop(0)
            if self.length>1:
                first.next.prev = None
            self.length -= 1 
        else:
            print("List is empty")
        
    def deleteLast(self):
        # リストの末尾の要素を削除する。        
        if not self.isEmpty():
            last = self.linkedlist.pop()
            if self.length>1:
                last.prev.next = None
            self.length -= 1 
        else:
            print("List is empty")
        
    def print(self):
        if not self.isEmpty():
            print(' '.join([node.key for node in self.linkedlist]))
        else:
            print('')

def main():
    input()
    n = 1786329# int(input())
    # n = int(input())
    commands = (input() for i in range(n)) # generator式リスト内包表記
    # commands = ({'order': c[0], 'value': c[1]} if len(c)==2 else {'order': c[0]} for c in commands)
    dll = MyDLL()
    # for c in commands:
    #     if c['order']=='insert':
    #         dll.insert(c['value'])
    #     elif c['order']=='delete':
    #         dll.delete(c['value'])
    #     elif c['order']=='deleteFirst':
    #         dll.deleteFirst()
    #     elif c['order']=='deleteLast':
    #         dll.deleteLast()
    #     else:
    #         print("the command dont't exist")
    #         print(c)
    for c in commands:
        if 'insert' in c:
            dll.insert(c.split()[1])
        elif 'deleteFirst' in c:
            dll.deleteFirst()
        elif 'deleteLast' in c:
            dll.deleteLast()
        elif 'delete' in c:
            dll.delete(c.split()[1])
        else:
            print("the command dont't exist")
            print(c)
    dll.print()    


if __name__=='__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print(elapsed)