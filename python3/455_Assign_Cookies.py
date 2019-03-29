#Big screen for better view.
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #给出两个list，List1 代表小孩想要的大小，List2 代表已有饼干的大小。能不能把 List2 的值尽可能地匹配给 List1。
        #同一个索引，如果 列表1 <= 列表2，就把饼干给出去，同时换下一个饼和人，如果不行，人不变且换更大的饼对比。

        #Imaging two list. U don't have to set another two instances in real life. 实际上你不需要多设置这两个list
        #I just do it for better understanding. 我只是为了方便理解。
        list1 = g
        list2 = s

        #Sort the two lists first. 先排序
        list1.sort()
        list2.sort()

        #Set index then. 设置索引
        index1 = 0
        index2 = 0

        #Compare the same index item between two lists.
        #If s[j] >= g[i], then give the cookie away.
        while index1 < len(list1) and index2 < len(list2):
            if list2[index2] >= list1[index1]:       #If not, don't give cookie, but change to the next child.
                index1 += 1
            index2 += 1          #Next element of list2, you have to try a bigger size.
        return index1
