class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        update =[]
        for i in range(len(nums)):
            if nums[i]!=val:
                update.append(nums[i])
        for i in range(len(update)):
            nums[i] = update[i]
        return len(nums[:len(update)])