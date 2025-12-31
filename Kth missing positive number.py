#https://leetcode.com/problems/kth-missing-positive-number/
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #Binary search-O(logn)
        
        # Idea: count how many numbers are missing till index mid
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            # Missing numbers till index mid
            # Expected value at index mid = mid + 1 because it starts from 1,2...
            # Actual value = arr[mid]
            # So missing = arr[mid] - (mid + 1)
            missing = arr[mid]-(mid+1)
            if missing<k:
                # Means k-th missing number is on the right side
                # Left side lo chala takkuva missing unnayi
                low=mid+1
            else:
                # Enough missing numbers exist on the left side
                # So answer left side lo undi
                high=mid-1
        
        # After loop:
        # low = number of elements in arr which are <= k-th missing
        # Final answer = low + k
        #Final position = missing count + present count
        #Final value    = k + low

        return low+k   #high+1+k
        #“low represents how many array elements appear before the k-th missing number.
        #Since each present element shifts the missing sequence by one, the final answer is k + low.”


        #Linear search -O(n)
        # n=len(arr)
        # for i in range(n):
        #     if arr[i]<= k:   #If we have any number less than k then we will add +1 to k so when number 
        #         k+=1         # is greater than k then it will the answer.
        #     else:
        #         break
        # return k

    #Time-O(n)
    #Space-O(1)
