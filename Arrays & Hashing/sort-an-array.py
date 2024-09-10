#Merge Sort

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
# I went with the merge sort which basically divides the list up until we can't split anymore and then merge the
# values back together again, while making sure the merged section is sorted.

# Quicksort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(arr, left, right):
            pivot_index = random.randint(left, right)
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  
            pivot = arr[right] 
            i = left - 1 
            for j in range(left, right): 
                if arr[j] < pivot:
                    i += 1 
                    arr[j] , arr[i] = arr[i], arr[j]
            i += 1
            arr[i], arr[right] = arr[right], arr[i]
            return i 
      
        def quicksort(arr, left, right): 
            if(right <= left): 
                return 

            pivot = partition(arr, left, right) 
            quicksort(arr, left, pivot - 1) 
            quicksort(arr, pivot + 1, right)
        
        quicksort(nums, 0, len(nums) - 1)
        return nums

# another way to do this is to use quick sort, which essentially, picks a pivot which is the number for us to compare to 
# and at the end of the sorting, we will find the final position of the pivot. To do this, we go through all the values within a range,
# and when we find a value less than our pivot we will make sure to move it to the front of the list, and to keep track of this, we will
# use a variable that starts one before the left boundary that we are looking at, then only when we find a value smaller, will we increment 
# this variable. if we had set our variable at the the start of left instead of one less than left, we would then need to edit the algorithm 
# to make sure i is not incremented at the end or the pivor values would be wrong.