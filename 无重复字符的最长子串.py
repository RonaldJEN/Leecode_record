# 題目 : 给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。

# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # 如果字符串s为空，返回0
        if n == 0 :
            return 0
        # 保存窗口内字符串
        window = []
        # 最大子串长度
        max_len = 0
        # 当前子串长度
        cur_len = 0
        # 遍历字符串s
        for i in range(n):
            val = s[i]
            # 如果该值不在窗口中
            if not val in window:
                # 添加到窗口内
                window.append(val)
            # 如果该值在窗口中已存在
            else:
                # 获取其在窗口中的位置
                index = window.index(val)
                # 更新窗口數據(移除該位置之前的數據)
                window = window[index+1:]
                window.append(val)
            # 当前长度更新为窗口长度
            cur_len = len(window)
            # 如果当前长度大于最大长度，更新最大长度值
            if cur_len > max_len : 
                max_len = cur_len
        return max_len

