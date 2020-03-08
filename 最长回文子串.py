# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        n=len(s)
        # n*n 矩陣
        dp=[[False]*n for _ in range(n)]
        # 初始化
        max_len=1
        start=0
        for i in range(n):
            # 單個字符一定是回文子串
            dp[i][i]=True
            # i< n-1定義下界線
            if(i<n-1 and s[i]==s[i+1]):
                # 相鄰回文子串
                dp[i][i+1]=True
                start=i
                max_len=2
        # 遍歷長度3以上的回文子串
        for l in range(3,n+1): #(所有最長子串可能長度)
            for i in range(n+1-l): #(索引:從0開始,遍歷區間<n+1-l>->索引為i,長度為l,子串右側索引為 i+l-1,為了保證不越界,i+l-1<n -> i< n+1- l)
                # 令子串右側索引為
                r=i+l-1
                # 如果子串s[i+1,r-1]為回文且s[i]==s[r],則代表s[i,r]也為回文
                if(s[i]==s[r] and dp[i+1][r-1]):
                    dp[i][r]=True
                    start=i
                    max_len=l
        return s[start:start+max_len]
