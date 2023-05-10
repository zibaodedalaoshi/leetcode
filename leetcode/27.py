class Solution:
    def removeElement(nums, val) -> int:
        n = nums.count(val)
        for i in range(n):
            nums.remove(val)
        return nums

if __name__ == '__main__':
    a = Solution.removeElement([0,1,2,2,3,0,4,2],2)
    print(a)

#通过，时间击败7.2%，空间击败67.61%

'''
def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        slow = 0
        fast = 0
        while(fast < n):
            # 用来收集不等于的值，如果fast对应值不等于val, 则把它和slow替换，并让slow前进。
            if (nums[fast] != val):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

作者：倾其所有。
链接：https://leetcode.cn/problems/remove-element/solutions/2236045/tong-xiang-shuang-zhi-zhen-he-xiang-xian-m92e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''