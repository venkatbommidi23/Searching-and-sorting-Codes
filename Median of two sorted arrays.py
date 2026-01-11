#https://www.naukri.com/code360/problems/median-of-two-sorted-arrays_985294?leftPanelTabValue=PROBLEM

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n))
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.





def median(nums1: int, nums2: int) -> float:
    
#Concept:
# 1) Binary Search ni eppudu chinna array meeda apply cheyyali
#    (min length array use cheste time complexity thaggutundi)

# 2) Goal: arrays ni two partitions ga divide cheyyadam
#    such that left side lo total elements = (n1 + n2 + 1) // 2

# 3) mid1 = nums1 lo partition index
#    mid2 = left - mid1 (nums2 lo corresponding partition)

# 4) l1, l2 = left partitions lo unna last (max) elements
#    r1, r2 = right partitions lo unna first (min) elements

# 5) Boundary cases handle cheyyadaniki:
#    partition start ayithe l = -infinity
#    partition end ayithe r = +infinity

# 6) Correct partition condition:
#    l1 <= r2 AND l2 <= r1
#    (left side lo anni values right side kanna chinnavi undali)

# 7) Correct partition dorikithe:
#    - total length even ayithe:
#      median = (max(l1, l2) + min(r1, r2)) / 2
#    - total length odd ayithe:
#      median = max(l1, l2)

# 8) l1 > r2 ayithe:
#    nums1 partition ekkuva right lo undi
#    so high = mid1 - 1 (left ki move cheyyali)

# 9) l2 > r1 ayithe:
#    nums1 partition chala left lo undi
#    so low = mid1 + 1 (right ki move cheyyali)

# 10) Final result without merging arrays
#     Time: O(log(min(n1, n2)))
#     Space: O(1)


        # Lengths of both arrays
        n1=len(nums1)
        n2=len(nums2)

        # Always apply binary search on smaller array
        if n1 > n2:
            return median(nums2,nums1)
        low=0
        high=n1
        while low<=high :
            # Partition index for nums1
            mid1=(low+high)//2

            # Total elements required on left side
            # left side lo undalsina total elements
            left=(n1+n2+1)//2

            # Partition index for nums2
            mid2= left - mid1

            # Left max values
            # partition left side last element            
            l1=float('-inf') if mid1==0  else nums1[mid1-1]
            l2=float('-inf') if mid2==0  else nums2[mid2-1]

            # Right min values
            # partition right side first elements            
            r1=float('inf')  if mid1==n1 else nums1[mid1]
            r2=float('inf')  if mid2==n2 else nums2[mid2]


            # left side max <= right side min
            if l1<=r2 and l2<=r1:

                # Even total length
                if (n1+n2)%2==0:

                    # median = avg of max(left) and min(right)
                    return (max(l1,l2)+ min(r1,r2))/2.0
                else:
                    # Odd length ? max of left side
                    return float(max(l1,l2))

            # If l1 is too big, move left
            # nums1 partition left ki ekkuva undi
            elif l1 > r2:
                high=mid1-1
            # Else move right
            # nums1 partition right ki move avvali
            else:
                low=mid1+1
        return 0.0



        # Brute Force approach to find median of two sorted arrays
        # Time Complexity: O(m + n)  --> merging both arrays
        # Space Complexity: O(m + n) --> extra array used to store merged result

        arr = []          # merged sorted array ni store cheyyadaniki
        i = 0             # pointer for nums1
        j = 0             # pointer for nums2

        m = len(nums1)    # nums1 length
        n = len(nums2)    # nums2 length

        # Merge both arrays until one array is exhausted
        # rendu arrays lo chinna element ni arr lo add chestam
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])   # nums1 lo chinna element add
                i += 1                 # nums1 pointer move
            else:
                arr.append(nums2[j])   # nums2 lo chinna element add
                j += 1                 # nums2 pointer move

        # nums1 lo migilina elements ni add cheyyadam
        while i < m:
            arr.append(nums1[i])
            i += 1

        # nums2 lo migilina elements ni add cheyyadam
        while j < n:
            arr.append(nums2[j])
            j += 1

        l = len(arr)      # merged array length

        # If length is even, median = average of two middle elements
        # even length aithe rendu middle elements average
        if l % 2 == 0:
            return (arr[l // 2] + arr[(l // 2) - 1]) / 2

        # If length is odd, median = middle element
        # odd length aithe direct middle element
        else:
            return float(arr[l // 2])





        # Brute Force approach to find median of two sorted arrays
        # Time Complexity: O(m + n)  --> merging both arrays
        # Space Complexity: O(m + n) --> extra array used to store merged result

        arr = []          # merged sorted array ni store cheyyadaniki
        i = 0             # pointer for nums1
        j = 0             # pointer for nums2

        m = len(nums1)    # nums1 length
        n = len(nums2)    # nums2 length

        # Merge both arrays until one array is exhausted
        # rendu arrays lo chinna element ni arr lo add chestam
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])   # nums1 lo chinna element add
                i += 1                 # nums1 pointer move
            else:
                arr.append(nums2[j])   # nums2 lo chinna element add
                j += 1                 # nums2 pointer move

        # nums1 lo migilina elements ni add cheyyadam
        while i < m:
            arr.append(nums1[i])
            i += 1

        # nums2 lo migilina elements ni add cheyyadam
        while j < n:
            arr.append(nums2[j])
            j += 1

        l = len(arr)      # merged array length

        # If length is even, median = average of two middle elements
        # even length aithe rendu middle elements average
        if l % 2 == 0:
            return (arr[l // 2] + arr[(l // 2) - 1]) / 2

        # If length is odd, median = middle element
        # odd length aithe direct middle element
        else:
            return float(arr[l // 2])
