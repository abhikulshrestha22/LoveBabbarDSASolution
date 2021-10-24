# Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array/#

class Solution:
    def search(self, nums, target):
        return self.search_recursive(nums, 0, len(nums)-1, target)

    def search_recursive(self, nums, low, high, target):
        if low >= high:
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            if target <= nums[low]:
                return self.search_recursive(nums, mid, high, target)
            else:
                return self.search_recursive(nums, low, mid-1, target)
        else:
            if target <= nums[low]:
                return self.search_recursive(nums, low, mid, target)
            else:
                return self.search_recursive(nums, mid+1, high, target)
