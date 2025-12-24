from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        """字符串方法

        Args:
            x (int): _description_

        Returns:
            int: _description_
        """
        if x <0:
            x = -x
            str_num = str(x)
            str_num = str_num[::-1]
            x = int(str_num)
            x = -x
        elif x > 0:
            str_num = str(x)
            str_num = str_num[::-1]
            x = int(str_num)
        if x == 0 or  x <= -2**31 or x >= 2**31 -1:
            x = 0
        return x
    def reverse2(self, x: int) -> int:
        """通过数据操作实现反转
        Args:
            x (int): _description_
        Returns:
            int: _description_
        """
        flag = False
        if x < 0:
            flag = True
            x = -x
        tmp_x = x
        reverse_x= 0
        while tmp_x !=0 :
            num = tmp_x % 10
            reverse_x = reverse_x * 10 + num
            tmp_x = tmp_x // 10
            if reverse_x <= -2**31 or reverse_x >= 2**31 -1:
                return 0
        if flag:
            reverse_x = -reverse_x
        return reverse_x
if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse2(-10))
    
