class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        myNumList = str(x)
        myNumListReverced = myNumList[::-1]
        if myNumList == myNumListReverced:
            print(f"Your number {x} is palindrome!")
        else:
            print(f"Your number {x} is not palindrome!")


myNum = str(input("Enter a number here: "))
sol = Solution()
sol.isPalindrome(myNum)