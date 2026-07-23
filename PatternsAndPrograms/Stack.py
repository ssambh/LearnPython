from collections import deque


class Stack:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_brackets = "({["
        closed_brackets = ")}]"

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in closed_brackets and not stack:
                return False
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
obj = Stack()
print(obj.isValid("()"))
