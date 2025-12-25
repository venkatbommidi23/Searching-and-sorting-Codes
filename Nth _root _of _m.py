#https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
# Input: n = 3, m = 8
# Output: 2
# Explanation: 23 = 8

class Solution:
    #Binary Search
    def nthRoot(self, n, m):
      #Helper function
        def fun(n,m,mid):
            ans=1
            # mid^n calculate chestunnam without overflow
            for i in range(1,n+1):
                ans=ans*mid
                if ans>m:
                    return 2 # mid^n > m → search left
            if ans==m:
                return 1  # exact match
            return 0      # mid^n < m → search right
        
        low=1
        high=m
        if  m==0:
            return 0
        if m==1:
            return 1
        # if n==0:
        #     return 1 if m==1 else -1
        
        while low<=high :

            mid=(low +high)//2
            if fun(n,m,mid)==1:
                return mid
            elif fun(n,m,mid)==2:
                high=mid-1
            else:
                low=mid+1
        return -1   
        
        #Time Complexity-O(nlogm)
        #Space=0(1)
     
