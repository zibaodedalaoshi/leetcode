class Solution:
    def checkDistances(s: str, distance: list) -> bool:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dic={}
        for i in range(len(distance)):
            dic[alphabet[i]] = distance[i]
        lst = list(s)
        result = 0
        for i in dic.keys():
            if lst.count(i) != 0:
                index1 = lst.index(i)
                index2 = lst.index(i,index1+1)
                reduction = index2 - index1 - 1
                if reduction == dic[i] :
                    result +=1
        return result == len(lst)/2

if __name__ == '__main__':
    s = "abaccb"
    distance = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a = Solution.checkDistances(s,distance)
    print(a)

#通过，时间击败6.63%，空间击败46.99%

"""
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        return all(len(s.split(c)[1]) == distance[ord(c) - 97] for c in set(s))
"""
