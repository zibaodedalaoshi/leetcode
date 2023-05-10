class Solution:
    def removeDuplicates(nums) -> int:
        if len(nums) ==1:
            return 1
        slow = 0
        fast = 1
        while slow<fast and fast<len(nums):
            if nums[slow]==nums[fast]:
                nums.pop(fast)
            else:
                fast+=1
                slow+=1
        return nums

if __name__ == '__main__':
    a = Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(a)

#通过，时间击败11.84%，空间击败44.17%