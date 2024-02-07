class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        tmp_list = list(nums)
        for i in range(len(nums)):
            tmp_list.pop(0)
            if (target - nums[i]) in tmp_list:
                result.append(i)
                result.append(self.find(nums, target, i))
                return result
            else:
                pass

    def find(self, nums, target, j):
        for i in range(j+1, len(nums)):
            if target - nums[i] == nums[j]:
                return i
            else:
                pass

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))