right_brackets = ['(', '[', '{']
left_brackets = [')', ']', '}']
brackets_dic = {"(":0, ")":0, '[':1, ']':1, '{':2, '}':2}


class Solution:
    def isValid(self, s: str) -> bool:
        right = []
        left = []
        brackets_stack = []
        first_situation = 0
        second_situation = 0
        if len(s) % 2 != 0:
            return False
        
        '''################
        Method 2
        ################'''
        for i in range(len(s)):
            if s[i] in right_brackets:
                brackets_stack.append(s[i])
                continue
            else:
                try:
                    if brackets_dic[s[i]] == brackets_dic[brackets_stack[-1]]:
                        brackets_stack.pop()
                        continue
                    else:
                        return False
                except:
                    return False
        if brackets_stack == []:
            return True
        else:
            return False


        '''################
        Method 1
        ################'''
        '''
        for i in range(len(s)):
            if s[i] in right_brackets:
                right.append(s[i])
                continue
            if s[i] in left_brackets:
                left.append(s[i])
                continue
        if len(right)  != len(left):
            return False
        else:
            for i in range(len(left)):
                if brackets_dic[right[i]] == brackets_dic[left[i]]:
                    first_situation += 1
                    pass
            
                elif brackets_dic[right[i]] == brackets_dic[left[len(left) - i - 1]]:
                    second_situation += 1
                else:
                    return False
            if first_situation == len(left) or second_situation == len(left):
                return True
            else:
                return False
        '''
    
result = Solution()
test_case = ["){", "()", "()[]{}", "(]", "{[]}", "([)]"]
print(result.isValid(test_case[0]))
