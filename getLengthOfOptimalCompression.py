from functools import wraps

try:
    from functools import lru_cache
except ImportError:
    def lru_cache(user_function):
        cache = {}
        @wraps(user_function)
        def wrapper(*args):
            key = tuple(args)
            if key not in cache:
                cache[key] = user_function(*args)
            return cache[key]
        return wrapper


class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        @lru_cache
        def counter(start, last, last_count, left):
            if left < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == last:
                if last_count == 1 or last_count == 9 or \
                    last_count == 99:
                    incr = 1
                else: incr = 0
                return incr + counter(start+1, last, last_count+1, left)
            else:
                keep_counter = 1 + counter(start+1, s[start], 1, left)
                del_counter = counter(start+1, last, last_count, left-1)
                return min(keep_counter, del_counter)
        return counter(0, "", 0, k)