class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1
        """
        s_list = list(s)
        dict_num = {}
        for i, stri in enumerate(s_list):
            if stri not in dict_num.keys():
                dict_num[stri] = 1
            else:
                dict_num[stri] += 1
        for key, value in dict_num.items():
            if value == 1:
                return s_list.index(key)
        return -1
        
        


if __name__ == '__main__':
    solution = Solution()
    # print(solution.firstUniqChar('leetcode'))
    print(solution.firstUniqChar('"loveleetcode"'))


