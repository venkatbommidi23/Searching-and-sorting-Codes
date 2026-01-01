#https://www.geeksforgeeks.org/problems/aggressive-cows/1

# Input: stalls[] = [1, 2, 4, 8, 9], k = 3
# Output: 3
# Explanation: The first cow can be placed at stalls[0], 
# the second cow can be placed at stalls[2] and 
# the third cow can be placed at stalls[3]. 
# The minimum distance between cows in this case is 3, which is the largest among all possible ways

class Solution:
    def aggressiveCows(self, stalls, k):
        #“Can I place k cows such that each cow is at least dist distance apart?”
        #dist distance maintain chesi k cows place cheyyagalama
        def canweplace(stalls,dist,k):
            n=len(stalls)
            cows=1                # First cow ni first stall lo place chestam
            last_pos=stalls[0]    # Last placed cow position
            
            # Remaining stalls ni check chestam
            for i in range(1,n):
                # Current stall ki last cow ki madhya distance >= dist unte
                if (stalls[i]-last_pos) >=dist:
                    cows+=1       # Next cow ni place chestam
                    last_pos=stalls[i]
                
                # k cows place ayyaka, inka check avasaram ledu
                if cows==k:
                    return True
            
            # k cows place cheyyalekapothe
            return False
            
        # When binary searching on minimum distance,
        # high = max_position − min_position          
        #Sorting is required for distance comparison      
        stalls.sort()
        low=1                        # Minimum possible distance
        high=stalls[-1]-stalls[0]    # Maximum possible distance
        while low<=high :
            mid=(low+high)//2
            # If we can place cows with distance = mid
            if canweplace(stalls,mid,k)==True:
                ans=mid            # mid valid answer
                low=mid+1          # Inka better (bigger) distance try chestam
            else:
                high=mid-1         # Distance reduce chestam
                
        return ans  #We can directly return high without ans,because
                    #ans is present at index high
                    
                    
        #Time-O(nlogn)-for sorting
              # +O(nlog(maxdistance))--- O(n) for canweplace function and log(maxdistance is for binary search)
        #We can write O(nlogn) --O(nlogmaxdistance is small)
        
        #Space-O(1)
        
            
