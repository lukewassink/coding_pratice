# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


def parensAreValid(s):
    stack = []
    for c in s:
        if c in ['[', '(', '{']:
            stack.append(c)
            continue
        elif not stack: return False
        
        match c:
            case ']':
                if stack.pop() != '[': return False
            case ')':
                if stack.pop() != '(': return False
            case '}':
                if stack.pop() != '{': return False
            case _:
                return False

    return not stack

print(parensAreValid("([])[]({})") == True)
print(parensAreValid("([)]") == False)
print(parensAreValid("((()") == False)
