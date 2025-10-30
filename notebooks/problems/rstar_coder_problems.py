problems = {
    "twoSum": {
        "question": """
            ### Question:
            Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
            You may assume that each input would have exactly one solution, and you may not use the same element twice.
            You can return the answer in any order. If no two numbers add up to target return None.
            
            Example 1:

            Input: nums = [2,7,11,15], target = 9
            Output: [0,1]
            Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

            Example 2:

            Input: nums = [3,2,4], target = 6
            Output: [1,2]

            Example 3:

            Input: nums = [3,3], target = 6
            Output: [0,1]

            
            Constraints:

            2 <= nums.length <= 104
            -109 <= nums[i] <= 109
            -109 <= target <= 109
            Only one valid answer exists.

            
            Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

            ### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
            ```python
            class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
            ```

            ### Answer: (use the provided format with backticks)
        """,
        "test_cases": [
            { "input": "nums = [2,7,11,15]\ntarget = 9", "output": "[0,1]" },
            { "input": "nums = [3,2,4]\ntarget = 6", "output": "[1,2]" },
            { "input": "nums = [3,3]\ntarget = 6", "output": "[0,1]" },
            { "input": "nums = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]\ntarget = 58", "output": "[13, 14]" },
            { "input": "nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\ntarget = 1700", "output": "[7, 8]" },
            { "input": "nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]\ntarget = 10", "output": "[8, 9]" },
            { "input": "nums = [10,11,12,13,14,15,16,17,18,19,20]\ntarget = 30", "output": "[4, 6]" },
            { "input": "nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]\ntarget = -19", "output": "[8, 9]" },
            { "input": "nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\ntarget = 180", "output": "[7, 9]" },
            { "input": "nums = [5, 25, 15, 35, 45, 55, 65, 75, 85, 95]\ntarget = 100", "output": "[4, 5]" },
            { "input": "nums = [5,10,15,20,25,30,35,40,45,50]\ntarget = 95", "output": "[8, 9]" },
            { "input": "nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]\ntarget = 20", "output": "[4, 5]" },
            { "input": "nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]\ntarget = 190", "output": "[0, 1]" },
            { "input": "nums = [100,200,300,400,500,600,700,800,900,1000]\ntarget = 1500", "output": "[6, 7]" },
            { "input": "nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]\ntarget = 16", "output": "[6, 8]" },
            { "input": "nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ntarget = 19", "output": "[8, 9]" },
            { "input": "nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]\ntarget = 100", "output": "None" },
            { "input": "nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\ntarget = 9", "output": "[4, 5]" },
            { "input": "nums = [15, 8, 3, 12, 6, 4, 7]\ntarget = 20", "output": "[1, 3]" },
            { "input": "nums = [1,2,3,4,5,6,7,8,9,10]\ntarget = 19", "output": "[8, 9]" },
            { "input": "nums = [5, 25, 15, 75, 35, 65, 45, 85, 95, 105]\ntarget = 160", "output": "[3, 7]" },
            { "input": "nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]\ntarget = 38", "output": "None" },
            { "input": "nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]\ntarget = 0", "output": "[0, 1]" },
            { "input": "nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]\ntarget = 88", "output": "[9, 11]" },
            { "input": "nums = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97]\ntarget = 174", "output": "[7, 9]" },
            { "input": "nums = [1,3,5,7,9,11,13,15,17,19]\ntarget = 20", "output": "[4, 5]" },
            { "input": "nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\ntarget = 17", "output": "[0, 1]" },
            { "input": "nums = [9,8,7,6,5,4,3,2,1]\ntarget = 17", "output": "[0, 1]" },
            { "input": "nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]\ntarget = 2", "output": "[0, 1]" },
            { "input": "nums = [12, 22, 32, 42, 52, 62, 72, 82, 92, 102]\ntarget = 214", "output": "None" },
            { "input": "nums = [9, 1, 2, 3, 4, 5, 6, 7, 8]\ntarget = 17", "output": "[0, 8]" },
            { "input": "nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]\ntarget = 20", "output": "[0, 1]" },
            { "input": "nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]\ntarget = 85", "output": "[7, 8]" },
            { "input": "nums = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]\ntarget = 188", "output": "[8, 9]" },
            { "input": "nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]\ntarget = 294033", "output": "None" },
            { "input": "nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]\ntarget = 220", "output": "[9, 10]" },
            { "input": "nums = [23, 34, 45, 56, 67, 78, 89, 90, 100, 110]\ntarget = 179", "output": "[6, 7]" },
            { "input": "nums = [1, 5, 8, 14, 20, 26]\ntarget = 31", "output": "[1, 5]" },
            { "input": "nums = [100, 200, 300, 400, 500]\ntarget = 800", "output": "[2, 4]" },
            { "input": "nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\ntarget = 110", "output": "[4, 5]" },
            { "input": "nums = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]\ntarget = -19", "output": "[8, 9]" },
            { "input": "nums = [8, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\ntarget = 38", "output": "[17, 19]" },
            { "input": "nums = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50]\ntarget = -10", "output": "[1, 5]" },
            { "input": "nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]\ntarget = 1500", "output": "[6, 7]" },
            { "input": "nums = [50, 25, 75, 100, 125, 150, 175, 200, 225, 250]\ntarget = 300", "output": "[4, 6]" },
            { "input": "nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ntarget = 17", "output": "[7, 8]" },
            { "input": "nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]\ntarget = 9", "output": "[7, 8]" },
            { "input": "nums = [10, 20, 30, 40, 50, 60]\ntarget = 110", "output": "[4, 5]" },
            { "input": "nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\ntarget = 0", "output": "[0, 1]" },
        ]
    },
    "longestPalindrome": {
        "question": """
            ### Question:
            Given a string s, return the longest palindromic substring in s.
            
            Example 1:

            Input: s = "babad"
            Output: "bab"
            Explanation: "aba" is also a valid answer.

            Example 2:

            Input: s = "cbbd"
            Output: "bb"

            
            Constraints:

            1 <= s.length <= 1000
            s consist of only digits and English letters.



            ### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
            ```python
            class Solution:
            def longestPalindrome(self, s: str) -> str:
            ```

            ### Answer: (use the provided format with backticks)
        """,
        "test_cases": [
            { "input": "s = \"anana\"", "output": "anana" },
            { "input": "s = \"bbabbababa\"", "output": "babbab" },
            { "input": "s = \"abcba\"", "output": "abcba" },
            { "input": "s = \"\"", "output": "" },
            { "input": "s = \"noon high it is noon\"", "output": "noon" },
            { "input": "s = \"banana\"", "output": "anana" },
            { "input": "s = \"abcbcbcbcbcba\"", "output": "abcbcbcbcbcba" },
            { "input": "s = \"bbbbb\"", "output": "bbbbb" },
            { "input": "s = \"abc12321cba\"", "output": "abc12321cba" },
            { "input": "s = \"abacdfgdcaba\"", "output": "aba" },
            { "input": "s = \"madam\"", "output": "madam" },
            { "input": "s = \"aa\"", "output": "aa" },
            { "input": "s = \"abba\"", "output": "abba" },
            { "input": "s = \"aaaaa\"", "output": "aaaaa" },
            { "input": "s = \"raceacar\"", "output": "aca" },
            { "input": "s = \"ac\"", "output": "a" },
            { "input": "s = \"abbcccbbb\"", "output": "bbcccbb" },
            { "input": "s = \"12321\"", "output": "12321" },
            { "input": "s = \"mississippi\"", "output": "ississi" },
            { "input": "s = \"a\"", "output": "a" },
            { "input": "s = \"babad\"", "output": "aba" },
            { "input": "s = \"noon\"", "output": "noon" },
            { "input": "s = \"forgeeksskeegfor\"", "output": "geeksskeeg" },
            { "input": "s = \"abababa\"", "output": "abababa" },
            { "input": "s = \"neveroddoreven\"", "output": "neveroddoreven" },
            { "input": "s = \"aabbccddeedcbaabba\"", "output": "abba" },
            { "input": "s = \"noonhighnoon\"", "output": "noon" },
            { "input": "s = \"abcdefggfedcba\"", "output": "abcdefggfedcba" },
            { "input": "s = \"abcdedcba\"", "output": "abcdedcba" },
            { "input": "s = \"aaaa\"", "output": "aaaa" },
            { "input": "s = \"cbbd\"", "output": "bb" },
            { "input": "s = \"racecar\"", "output": "racecar" }
        ]
    }
}
