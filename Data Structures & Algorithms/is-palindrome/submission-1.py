class Solution:
    def isPalindrome(self, s: str) -> bool:
        unwanted_chars = "!@#$%^&*()_+=-[]{}\\|;:\'\",./<>?`~ "
        table = str.maketrans("", "", unwanted_chars)
        filtered = s.translate(table)
        filtered = filtered.lower()
        filteredR = filtered[::-1]
        print(filtered, filteredR)
        return filtered == filteredR