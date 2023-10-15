class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        q_cnt_1 = s1 = 0
        for i in range(n//2):    # get digit sum and question mark count for the first half of `num`
            if num[i] == '?':
                q_cnt_1 += 1
            else:    
                s1 += int(num[i])
        q_cnt_2 = s2 = 0				
        for i in range(n//2, n): # get digit sum and question mark count for the second half of `num`
            if num[i] == '?':
                q_cnt_2 += 1
            else:    
                s2 += int(num[i])
        s_diff = s1 - s2         # calculate sum difference and question mark difference
        q_diff = q_cnt_2 - q_cnt_1
        return not (q_diff % 2 == 0 and q_diff // 2 * 9 == s_diff) # When Bob can't win, Alice wins

# class Solution:
#     def sumGame(self, num: str) -> bool:
#         """
#             If Bob wants to win,
#             the number of '?' in input have to be even.
#             Otherwise, the game is finished by Alice,
#             Alice can win easily win.

#             If we add the same sum of digits to left and right,
#             this operation won't change the result.

#             If we add the same numnber of '?' with to left and right,
#             this operation won't change the result.

#             Example 1:
#             "??" = x
#             Bob can win if and only if x = 9.
#             x > 9, Alice makes "0?"
#             x < 9, Alice makes "9?"

#             Example 2:
#             "????" = y
#             Bob can win if and only if y = 9 * 2 = 18.
#             y > 18, Alice makes "0???",
#             and it becomes the case x > 9 in example 1
#             y < 18, Alice makes "9???",
#             and it becomes the case x < 9 in example 1.

#         """
#         return sum([1, -1][i < len(A) / 2] * (4.5 if c == '?' else int(c)) for i, c in enumerate(A)) != 0