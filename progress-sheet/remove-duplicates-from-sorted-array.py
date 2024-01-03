class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        setter = set()

        while left <= right:
            if nums[left] in setter:
                x = nums.pop(left)
                nums.append(x)
                right -= 1
            else:
                setter.add(nums[left])
                left += 1

        return left