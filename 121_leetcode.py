"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

Approach: 
Suppose for interval [i, j]:
    optI := buying price at prices[optI]
    optJ := selling price at prices[optJ]
    profit := prices[optJ] - prices[optI]

Then, for interval [i, j + 1]:
    if prices[j + 1] > prices[optJ]:
        optJ := j + 1
        profit := max(profit, prices[optJ] - prices[optI])

"""



"""
Algorithm based on Kadane's algorithm:

suppose from array from 1 : j, 
    f_opt(j) returns the maximum profit till j
    where prices[j] - prices[f_opt(j)] is the maximum profit

    We also maintain lowest price till j, i.e. prices[L(j)] is the lowest price in the interval [f_opt(j), j]

    Now for interval [f_opt(j), j+1]:
        a) profit = max(profit, prices[j+1] - f_opt(j)); if 
        b) max(profit, prices[j+1] - prices[L(j)])
            if (prices[j+1]-prices[L(j)]) > (profit), then
                f_opt(j+1) = L(j)
        c) if L[j+1] < L[j], then L[j+1] = L[j]



Exercise: Check correctness of the algorithm

"""