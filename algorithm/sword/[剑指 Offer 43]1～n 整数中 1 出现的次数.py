# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。 
# 
#  例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：6 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n < 2^31 
#  
# 
#  注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/ 
#  Related Topics 数学 
#  👍 122 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res
# leetcode submit region end(Prohibit modification and deletion)
