

# import numpy as np

# N = 2
# M = np.random.randint(20) + 1

# A = np.random.randint(500, size=N)
# A = np.sort(A)

# B = np.random.randint(500, size=M)
# B = np.sort(B)
# print(f"Len(A) = {N}, Med(A) = {A[N//2]}, A: ", A.reshape((N,)))
# print(f"Len(B) = {M}, Med(B) = {B[M//2]}, B: ", B.reshape((M,))) 

# # Returns index of x in arr if present, else -1
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0

#     while low <= high:

#         mid = (high + low) // 2

#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1

#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1

#         # means x is present at mid
#         else:
#             return mid

#     # If we reach here, then the element was not present
#     return low

# def swap(v1, v2):
#     v0 = v1
#     v1 = v2
#     v2 = v0
#     return v1, v2

# ### 

# # code to handle the case when the length of the array is <= 2 (either A or B)
# if N == 0 and M != 0:
#     if M % 2 == 0:
#         med = (B[M//2-1] + B[M//2])/2
#     else:
#         med = B[M//2]
# elif M == 0 and N != 0:
#     if N % 2 == 0:
#         med = (A[N//2-1] + A[N//2])/2
#     else:
#         med = A[N//2]
# elif N == 1 and M == 1:
#     med = (A[0] + B[0])/2
# elif N == 0 and M == 0:
#     med = float('nan')

# # initialization of pointers
# i1, j1 = 0, N-1
# i2, j2 = 0, M-1

# k1 = (j1-i1+1) # length of eff-array A
# k2 = (j2-i2+1) # length of eff-array B

# # loop until either of the array pointers points to array of size 2
# while k1 > 2 and k2 > 2:

#     medA = A[i1 + (j1-i1)//2]
#     medB = B[i2 + (j2-i2)//2]

#     if medA > medB:
#         A, B = swap(A, B)
#         i1, i2 = swap(i1, i2)
#         j1, j2 = swap(j1, j2)
#         k1, k2 = swap(k1, k2)            
#     # remove initial parts of eff-array A
#     # remove final parts of eff-array B
#     # update pointers
#     if k1 <= k2:
#         k = (j1-i1)//2
#         i1 = i1 + k
#         j2 = j2 - k         
#     else:
#         k = (j2-i2)//2
#         i1 = i1 + k
#         j2 = j2 - k

#     k1 = (j1-i1+1) # length of eff-array A
#     k2 = (j2-i2+1) # length of eff-array B



# Aa = A[i1:(j1+1)]
# Ba = B[i2:(j2+1)]
# if k2 <= 2:
#     Aa, Ba = swap(Aa, Ba)
#     i1, i2 = swap(i1, i2)
#     j1, j2 = swap(j1, j2)
#     k1, k2 = swap(k1, k2)            

# print(Aa, Ba)
# Ca = np.sort(np.concatenate([Aa, Ba]))
# print("Length (Ca) = %d"%(len(Ca)), Ca)

# if len(Aa) == 1:
#     I = binary_search(Ba, Aa[0])
#     print(Aa, Ca[I])
#     assert (Ca[I] == Aa[0])     

#     # if len(Ba) % 2 == 0:
#     #     # Final array would be odd-length
#     #     z = 0
#     # else:
#     #     # Final array would be even-length
#     #     z = 0
# else:
#     I = binary_search(Ba, Aa[0])
#     J = binary_search(Ba, Aa[1])
#     print(I, J+1)
#     print(Aa, Ca[I], Ca[J+1])
#     assert (Ca[I] == Aa[0])
#     assert (Ca[J+1] == Aa[1])




# In[]:


import numpy as np
import time 
from scipy import io as sio

MS_all = []
T_all = []
for mS in range(10, 5000, 500):
    MS = []
    T = []
    for it in range(10000):
        N = np.random.randint(mS) + 1
        M = np.random.randint(mS) + 1

        A = np.random.randint(10000, size=N)
        A = np.sort(A)

        B = np.random.randint(10000, size=M)
        B = np.sort(B)

        C = np.sort(np.concatenate([A, B]))
        print(f"Len(A) = {N}, Med(A) = {A[ N//2]}, A: ", A.reshape((N,)))
        print(f"Len(B) = {M}, Med(B) = {B[ M//2]}, B: ", B.reshape((M,)))
        print(f"Len(C) = {len(C)}, Med(C) = {np.median(C)}, C: ", C.reshape((len(C),)))

        # Returns index of x in arr if present, else -1
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:

                mid = (high + low) // 2

                # If x is greater, ignore left half
                if arr[mid] < x:
                    low = mid + 1

                # If x is smaller, ignore right half
                elif arr[mid] > x:
                    high = mid - 1

                # means x is present at mid
                else:
                    return mid

            # If we reach here, then the element was not present
            return low


        def swap(v1, v2):
            v0 = v1
            v1 = v2
            v2 = v0
            return v1, v2

        ###

        st = time.time()
        # code to handle the case when the length of the array is <= 2 (either A or B)
        if N == 0 and M != 0:
            if M % 2 == 0:
                medComp = (B[M // 2 -1] + B[M//2] ) /2
            else:
                medComp = B[ M//2]
        elif M == 0 and N != 0:
            if N % 2 == 0:
                medComp = (A[N // 2 - 1] + A[ N//2] ) /2
            else:
                medComp = A[ N // 2]
        elif N == 1 and M == 1:
            medComp = (A[0] + B[0]) /2
        elif N == 0 and M == 0:
            medComp = float('nan')

        # initialization of pointers
        i1, j1 = 0, N- 1
        i2, j2 = 0, M - 1

        k1 = (j1 - i1 + 1)  # length of eff-array A
        k2 = (j2 - i2 + 1)  # length of eff-array B

        # loop until either of the array pointers points to array of size 2
        while k1 > 2 and k2 > 2:

            medA = A[i1 + (j1 - i1) // 2]
            medB = B[i2 + (j2 - i2) // 2]

            if medA > medB:
                A, B = swap(A, B)
                i1, i2 = swap(i1, i2)
                j1, j2 = swap(j1, j2)
                k1, k2 = swap(k1, k2)
                # remove initial parts of eff-array A
            # remove final parts of eff-array B
            # update pointers
            if k1 <= k2:
                k = (j1 - i1) // 2
                i1 = i1 + k
                j2 = j2 - k
            else:
                k = (j2 - i2) // 2
                i1 = i1 + k
                j2 = j2 - k

            k1 = (j1 - i1 + 1)  # length of eff-array A
            k2 = (j2 - i2 + 1)  # length of eff-array B

        Aa = A[i1:(j1 + 1)]
        Ba = B[i2:(j2 + 1)]
        if k2 <= 2:
            Aa, Ba = swap(Aa, Ba)
            i1, i2 = swap(i1, i2)
            j1, j2 = swap(j1, j2)
            k1, k2 = swap(k1, k2)

        # print(Aa, Ba)
        # Ca = np.sort(np.concatenate([Aa, Ba]))
        # print("Length (Ca) = %d" % (len(Ca)), Ca)

        if len(Aa) == 1:
            I = binary_search(Ba, Aa[0])
            # print(Aa, Ca[I])

            # if len(Ba) % 2 == 0:
            #     # Final array would be odd-length
            #     z = 0
            # else:
            #     # Final array would be even-length
            #     z = 0
        else:
            I = binary_search(Ba, Aa[0])
            J = binary_search(Ba, Aa[1]) + 1
        
        ed = time.time()

        if len(Aa) == 2:
            lenBa = len(Ba)
            if lenBa % 2 == 0:
                medBa1 = Ba[lenBa//2-1]
                medBa2 = Ba[lenBa//2]
                if Aa[1] <= medBa1:
                    if J == ((lenBa+2)//2-1):
                        z1 = Aa[1]
                    else:
                        z1 = Ba[lenBa//2-2]
                    z2 = medBa1
                elif (Aa[1] > medBa1) and (Aa[1] <= medBa2) and (Aa[0] <= medBa1):
                    z1 = medBa1
                    z2 = Aa[1]
                elif (Aa[0] <= medBa1) and (Aa[1] > medBa2):
                    z1 = medBa1
                    z2 = medBa2
                elif (Aa[0] > medBa1) and (Aa[1] <= medBa2):
                    z1 = Aa[0]
                    z2 = Aa[1]
                elif (Aa[0] > medBa1) and (Aa[0] <= medBa2):
                    z1 = Aa[0]
                    z2 = medBa2
                elif Aa[0] > medBa2:
                    z1 = medBa2
                    if I == ((lenBa+2)//2):
                        z2 = Aa[0]
                    else:
                        z2 = Ba[lenBa//2+1]
                # print("Z1 = %d, Z2 = %d"%(z1, z2))
                medComp = (z1 + z2)/2
            else:
                medBa = Ba[lenBa//2]

                if Aa[1] <= medBa:
                    if J == ((lenBa+2)//2):
                        z = Aa[1]
                    else:
                        z = Ba[lenBa//2-1]
                elif (Aa[0] <= medBa) and (Aa[1] > medBa):
                    z = medBa
                elif Aa[0] > medBa:
                    if I == ((lenBa+2)//2):
                        z = Aa[0]
                    else:
                        z = Ba[lenBa//2+1]
                # print("Z = %d"%(z))
                medComp = z
        else:
            lenBa = len(Ba)
            if lenBa % 2 == 0:
                medBa1 = Ba[lenBa//2-1]
                medBa2 = Ba[lenBa//2]
                if Aa[0] <= medBa1:
                    # if I == ((lenBa+1)//2):
                    #     z = Aa[0]
                    # else:

                    z = medBa1
                elif (Aa[0] > medBa1) and (Aa[0] <= medBa2):
                    z = Aa[0]
                elif Aa[0] > medBa2:
                    z = medBa2
                # print("Z = %d"%(z))
                medComp = z
            else:
                medBa = Ba[lenBa//2]

                if Aa[0] <= medBa:
                    if I == ((lenBa+1)//2-1):
                        z1 = Aa[0]
                    else:
                        z1 = Ba[lenBa//2-1]
                    z2 = medBa
                elif Aa[0] > medBa:
                    if I == ((lenBa+1)//2):
                        z2 = Aa[0]
                    else:
                        z2 = Ba[lenBa//2+1]
                    z1 = medBa
                # print("Z1 = %d, Z2 = %d"%(z1, z2))
                medComp = (z1 + z2)/2


        # print("Ori median = %f, Comp median = %f"%(np.median(C), medComp))
        assert np.allclose(np.median(C), medComp, rtol=1e-5, atol=1e-8)
        MS.append(M+N)
        T.append(ed-st)
    MS_all.append(MS)
    T_all.append(T)

sio.savemat('4b_leetcode.mat', mdict = {'MS': MS_all, 'T': T_all})