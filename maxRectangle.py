
# """
# # You are given an integer array height of length n. 
# # There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[il).
# # Find two lines that together with the x-axis form a container, such that the container contains the most water.

# The problem is to find two vertical lines from the given array of heights such that they form a container 
# with the x-axis and maximize the amount of water that can be stored in the container. 
# The height of each line is given by the corresponding element in the array. 
# The goal is to find the maximum possible area of water that can be contained within the 
# container formed by the two lines.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1, 8, 6, 2, 5, 4, 8, 3, 7]. 
# In this case, the max area of water (blue section) the container can contain is 49.
# """
# import pdb 
# import numpy as np
# # #pdb.set_trace()


# # N = 9
# # # write code to write table to excel in different sheets
# # import pandas as pd
# # import openpyxl
# # writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='openpyxl')

# # for it in range(5):
# #     # A = np.array([1, 8, 6, 2, 5])
# #     A = np.round(np.random.random(N) * 100, 0)
# #     Z = np.ones((N-1, N-1)) * np.nan
# #     Z_a = np.ones((N-1, N-1)) * np.nan
# #     Z_a_r = np.ones((N-1, N-1)) * np.nan
# #     Z_r = np.ones((N-1, N-1)) * np.nan
# #     for i in range(N-1): # for elements in A
# #         for j in range(1, N-i): # distance from i
# #             Z[i, j-1] = min(A[i], A[i + j])
# #             Z_a[i, j-1] = Z[i, j-1] * j
# #             Z_a_r[i, j-1] = np.round(np.random.random(1) * 10, 2)
# #             Z_r[i, j-1] = np.round(Z_a_r[i, j-1]/j, 2)
# #     print(A)
# #     print("#"*50, "Z", "#"*50)
# #     # print(Z)
# #     # print("#"*50, "Z_a", "#"*50)
# #     # print(Z_a)
# #     # print("#"*50, "Z_a_r", "#"*50)
# #     # print(Z_a_r)
# #     # print("#"*50,  "Z_r", "#"*50)
# #     # print(Z_r)


# #     # Create a Pandas Excel writer using XlsxWriter as the engine.

# #     # Write each dataframe to a different worksheet.
# #     Z_df = pd.DataFrame(Z_r)

# #     Z_df.to_excel(writer, sheet_name='E%d'%(it))

# #     # Close the Pandas Excel writer and output the Excel file.
# #     writer.save()

# # writer.close()

# """
# 1. Suppose i_opt and j_opt(i_opt) are the indices of the maximum area container where i_opt < j_opt.
# 2. Suppose two pointers p1 and p2, pointing to the ith and jth element of the array with i < j.
# 3. Property 1: for p1 <= i_opt, the maximum area is contained within the container formed by p1 and 
#                     j_opt(p1).
        
# """

# N = 100
# nIters = 10000
# b = np.zeros((nIters, 1))
# for it in range(nIters):
    
#     A = np.round(np.random.random(N) * 100, 0)


#     i_opt = 0
#     j_opt = N-1
#     A_max = 0
#     for k1 in range(N):
#         for k2 in range(k1+1, N):
#             if A[k1] < A[k2]:
#                 if (k2 - k1) * A[k1] > A_max:
#                     i_opt = k1
#                     j_opt = k2
#                     A_max = (k2 - k1) * A[k1]
#             else:
#                 if (k2 - k1) * A[k2] > A_max:
#                     i_opt = k1
#                     j_opt = k2
#                     A_max = (k2 - k1) * A[k2]
#     # print(A)
#     # print("I = [%d-%d]"%(i_opt, j_opt), "A[i_opt] = %d, A[j_opt] = %d, MaxRectArea = %f"%(A[i_opt], A[j_opt], (j_opt - i_opt) * min(A[i_opt], A[j_opt])))


#     i_opt = 0
#     j_opt1 = N-1
#     A_max = 0
#     k1 = 0
#     for k2 in range(k1+1, N):
#         if A[k1] < A[k2]:
#             if (k2 - k1) * A[k1] > A_max:
#                 i_opt = k1
#                 j_opt1 = k2
#                 A_max = (k2 - k1) * A[k1]
#         else:
#             if (k2 - k1) * A[k2] > A_max:
#                 i_opt = k1
#                 j_opt1 = k2
#                 A_max = (k2 - k1) * A[k2]
#     # print("I = [%d-%d]"%(i_opt, j_opt), "A[i_opt] = %d, A[j_opt] = %d, MaxRectArea = %f"%(A[i_opt], A[j_opt], (j_opt - i_opt) * min(A[i_opt], A[j_opt])))
#     print("j_opt = %d, j_opt1 = %d, j_opt <= j_opt1 = %s"%(j_opt, j_opt1, j_opt <= j_opt1))
#     b[it] = (j_opt <= j_opt1)


# print(np.sum(b)/nIters)

def on2_solution_old(A):
    """
    Finds the indices of the optimal subarray and its maximum area in a 1D array using a nested loop approach.

    Args:
        A: A list of numbers representing the heights of a 1D array.

    Returns:
        A tuple containing three elements:
            - The index of the first element in the optimal subarray (inclusive).
            - The index of the last element in the optimal subarray (inclusive).
            - The maximum area of the optimal subarray.
    """

    n = len(A)
    i_opt, j_opt, A_max = 0, 0, 0

    for k1 in range(n):
        for k2 in range(k1 + 1, n):
            area = (k2 - k1) * min(A[k1], A[k2])  # Calculate area efficiently using min
            if area > A_max:
                i_opt = k1
                j_opt = k2
                A_max = area
                # print(area)
    return i_opt, j_opt, A_max

def on2_solution(A):
    N = A.shape[0]
    i_opt = 0
    j_opt = N-1
    A_max = 0
    for k1 in range(N):
        for k2 in range(k1+1, N):
            if A[k1] < A[k2]:
                if ((k2 - k1) * A[k1]) > A_max:
                    i_opt = k1
                    j_opt = k2
                    A_max = (k2 - k1 + 1) * A[k1]
            else:
                if ((k2 - k1) * A[k2]) > A_max:
                    i_opt = k1
                    j_opt = k2
                    A_max = (k2 - k1 + 1) * A[k2]
    return [i_opt, j_opt, A_max]
def on1_solution(A):
  """
  Finds the indices of the optimal subarray and its maximum area in a 1D array.

  Args:
      A: A list of numbers representing the heights of a 1D array.

  Returns:
      A tuple containing three elements:
          - The index of the first element in the optimal subarray (inclusive).
          - The index of the last element in the optimal subarray (inclusive).
          - The maximum area of the optimal subarray.
  """

  n = len(A)
  i_opt, j_opt, A_max = 0, n - 1, 0
  p1, p2 = 0, n - 1

  while True:
    if A[p1] <= A[p2]:
      cr_area = (p2 - p1 + 1) * min(A[p1], A[p2])
      if cr_area >= A_max:
        i_opt, j_opt, A_max = p1, p2, cr_area
      p1 += 1
    else:
      cr_area = (p2 - p1 + 1) * min(A[p1], A[p2])
      if cr_area >= A_max:
        i_opt, j_opt, A_max = p1, p2, cr_area
      p2 -= 1
    # print(A_max)
    if p1 > p2:
      break

  return i_opt, j_opt, A_max

# Example usage
import numpy as np
N = 10
A = np.random.random((N,)).astype(np.float64) * 100
print(A)
i, j, area = on2_solution(A)
print(f"Optimal subarray indices: ({i}, {j})")
print("Maximum area: %f"%(area))
print(A)
i, j, area = on1_solution(A)
print(f"Optimal subarray indices: ({i}, {j})")
print("Maximum area: %f"%(area))
