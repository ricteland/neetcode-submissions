class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        pal = [i for i in s if i.isalnum()]

        start, end = 0, len(pal) -1

        while start <= end:
            print(pal[start], pal[end])
            if pal[start].lower() == pal[end].lower():
                start += 1
                end -= 1

            else:
                return False

        return True
            