from collections import defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict_word = defaultdict(int)
        for i in words:
            dict_word[i] += 1
        word_l = len(words[0])
        all_word_l = len(words) * word_l
        result = []
        len_words = len(words)
        
        for i in range(len(s)):
            tmp = dict_word.copy()
            count_tmp = len_words
            while count_tmp:
                w = s[i + (len_words - count_tmp)*word_l:i + (len_words - count_tmp+1)*word_l]
                if tmp[w] > 0:
                    tmp[w] -= 1
                else:
                    break
                count_tmp -= 1
                if count_tmp == 0:
                    result.append(i)
            
        return result