#https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Allocation can be done in following ways:
# => [12] and [34, 67, 90] Maximum Pages = 191
# => [12, 34] and [67, 90] Maximum Pages = 157
# => [12, 34, 67] and [90] Maximum Pages = 113.
# The third combination has the minimum pages assigned to a student which is 113.



class Solution:
    def findPages(self, arr, k):
        
        # Helper function to count how many students are needed 
        # if no student can read more than 'pages' pages.
        def CountStudents(pages):
            students=1         # Start with one student
            pageStudent=0      # Track pages assigned to current student
            for i in range(len(arr)):
                
                 # If adding the current book doesn’t exceed limit, assign it
                if (arr[i]+pageStudent <=pages):
                    pageStudent+=arr[i]
                else:
                    # Otherwise, assign to the next student
                    students+=1
                    pageStudent=arr[i]  # Start counting pages for next student
            return students
        
        
        # Edge case: if number of students is greater than number of books
        if k > len(arr):
            return -1
        
        # Minimum pages any student must read = largest single book
        low=max(arr)
        # Maximum pages any student might read = sum of all books (1 student)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            count=CountStudents(mid)  # Check how many students are needed
            
            # If current limit allows k or fewer students,
            # try to reduce the max pages further (go left)
            if count <= k:
                high=mid-1
            else:  # If more students are needed, increase the limit (go right)
                low=mid+1
                
        # 'low' is the minimum possible max pages allocation
        return low
        
        #Time Complexity-O(n × log(sum(arr)))
        #Space-O(1)
                
