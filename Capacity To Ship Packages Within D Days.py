  #https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
 
# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Given a ship capacity, calculate how many days are needed
        def no_days(capacity):
            days_needed=1   # At least one day is required
            load=0          # Current day's load
            for w in weights:
                # If adding current weight exceeds capacity,
                # new day start cheyyali
                if load +w > capacity:
                    days_needed+=1  # Move to next day
                    load=w          # Start new day with current weight
                else:
                    load+=w          # Add weight to current day
            return days_needed
        
        # Minimum capacity must be max weight (single package must fit)
        low=max(weights)
        # Maximum capacity can be sum of all weights (ship everything in one day)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            # If we can ship within given days using mid capacity
            if no_days(mid)<=days:
                # mid capacity works, try smaller capacity
                high=mid-1
            else:
                # mid capacity is too small, need bigger capacity
                low=mid+1
        # low will point to the minimum valid ship capacity
        return low

       #Time Complexity-O(nlog(s)) where n is len(weights) ,s is (sum of weights-min of weights) 
       #Space Complexity-O(1)
