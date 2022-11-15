# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
#         def compareWord(word):
#             index = 0
#             for char in word:
#                 while index < len(s) and s[index] != char:
#                     index += 1
#                 if index >= len(s):
#                     return False
#                 index += 1
#             return True
            
#         count = 0
#         for word in words:
#             if compareWord(word):
#                 count += 1
#         return count
                    
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count