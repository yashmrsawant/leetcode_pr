

"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.
 Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.



Dynamic Programming approach:

a) Given maximum array sum from index f_A(j) to index j, 

b) If current global maximum s(j-1) till index j-1; s(j-1) < f_A(j-1) + x(j), then
    s(j) = f_A(j-1) + x(j)

c) If current global maximum s(j-1) till index j-1; s(j-1) > f_A(j-1) + x(j), then
    s(j) = s(j-1)

d) f_A(j) = max(f_A(j-1) + x(j), x(j)) # dynamic update of maximum subarray sum till index j


Divide and Conquer approach:
a) Divide the array into two halves
b) Find maximum subarray sum in left half; return the start and end index of maximum subarray sum
c) Find maximum subarray sum in right half; return the start and end index of maximum subarray sum

-0.44, 0.11, -0.68, -0.33, 0.76, 0.64, 0.2, 0.86, -0.6, -0.29, 0.73, 0.62, 0.43, 0.84, 0.99, 
0.27, 0.98, 0.28, 0.92, -0.56, -0.32, -0.73, -0.13, -0.77, -0.8, 0.9, 0.84, -0.29, 0.11, 
0.53, 0.21, -0.36, -0.59, 0.29, 0.18, 0.2, 0.67, -0.48, 0.97, -0.17, 0.94, -0.8, -0.96, 
0.37, -0.32, 0.75, 0.92, 0.79, -0.67, 0.17, -0.43, 0.15, -0.17, 0.33, 0.29, 0.6, -0.15, 
-0.74, 0.03, -0.69, -0.77, -0.99, 0.63, 0.33, -0.66, -0.57, 0.44, -0.41, -0.33, -0.33, 
-0.45, 0.46, 0.55, -0.4, -0.83, -0.29, -0.43, 0.97, 0.1, -0.37, 0.55, -0.68, -0.06, 
-0.69, -0.91, -0.65, -0.16, -0.24, -0.77, 0.59, -0.61, -0.52, -0.78, -0.23, -0.12, 
-0.64, 0.48, 0.21, -0.97, -0.71

"""

import numpy as np
from matplotlib import pyplot as plt

N = 1000
# nums = [np.round(np.random.random(1)[0]*2-1, 2) for _ in range(N)]


R = np.random.randn(N)


plt.plot(R)
plt.show()



