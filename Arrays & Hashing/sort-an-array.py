class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, l, m, r): 
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0 
            while j < len(left) and k < len(right): 
                if left[j] <= right[k]: 
                    arr[i] = left[j]
                    j += 1
                else: 
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left): 
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right): 
                nums[i] = right[k]
                k += 1
                i += 1

        def mergesort(arr, l, r): 
            if l == r: 
                return arr
            
            m = (l + r) // 2
            mergesort(arr,l,m)
            mergesort(arr,m + 1,r)
            merge(arr, l, m, r)
        mergesort(nums,0,len(nums) - 1)
        return nums
    
# This question can be solved in many ways and this is just one of the ways to do this. We are simply asked
# to sort the given list in O(nlogn) time complexity so there are several ways to do this. For my solution, 
# I went with the merge sort which basically divides the list up until we can;t split anymore and then merge the
# values back together again, while making sure the merged section is sorted.