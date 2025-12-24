import typing
class Solution:
    def reverseString(self, s: typing.List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) -1 ] = s[len(s) -1 ], s[i]
        
        
if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    solution = Solution()
    solution.reverseString(s)
    print(s)