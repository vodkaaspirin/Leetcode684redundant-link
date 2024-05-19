class Solution(object):
    def findRedundantConnection(self, edges):
        class UnionFind:
            def __init__(self, n):   // UnionFind类的初始化方法，接受一个参数n，表示并查集的大小。
                self.parent = list(range(n + 1))  //初始化并查集的父节点数组，初始时每个节点的父节点是它自己。
                self.rank = [0] * (n + 1)  //初始化并查集的秩数组，初始时每个节点的秩都是0。

            def find(self, x):  // UnionFind类的find方法，用于查找节点x所在集合的根节点。
                if self.parent[x] != x:    //通过递归的方式找到节点x所在集合的根节点，并在查找过程中进行路径压缩。
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):	    //用于合并两个节点所在的集合
                root_x = self.find(x)  //找到节点x和节点y所在集合的根节点
                root_y = self.find(y)  //找到节点x和节点y所在集合的根节点
                if root_x == root_y:  //如果节点x和节点y已经在同一个集合
                    return False  //则返回False，表示合并失败
                if self.rank[root_x] < self.rank[root_y]:  //根据树的秩进行合并操作，以保持树的平衡
                    self.parent[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_y] = root_x
                    self.rank[root_x] += 1
                return True  	//返回True，表示合并成功

        n = len(edges) //创建并查集对象uf
        uf = UnionFind(n)  //传入边集合的大小n
        redundant_edge = None  初始化冗余边
        for edge in edges:  //遍历边集合，对每条边进行合并操作
            if not uf.union(edge[0], edge[1]):  //如果发现已经在同一个集合中
                redundant_edge = edge  //则将这条边标记为多余的边
        return redundant_edge //返回最后标记的多余边
