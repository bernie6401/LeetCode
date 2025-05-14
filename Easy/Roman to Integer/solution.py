class Solution:
    def __init__(self):
        self.roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        solution = 0
        if len(s) > 16 or len(s) == 0:
            exit()
        
        for i, j in enumerate(s):
            if j not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                exit()
            if i == 0:
                solution += self.roman_to_int[j]
            else:
                if self.roman_to_int[j] <= self.roman_to_int[s[i - 1]]:
                    solution += self.roman_to_int[s[i]]
                else:
                    solution += self.roman_to_int[s[i]] - 2 * self.roman_to_int[s[i - 1]]

        return solution
        

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))  # Output: 3
    print(s.romanToInt("IV"))   # Output: 4
    print(s.romanToInt("IX"))   # Output: 9
    print(s.romanToInt("LVIII")) # Output: 58
    print(s.romanToInt("MCMXCIV")) # Output: 1994