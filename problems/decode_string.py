class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        currs, currn = "", ""
        for c in s:
            if c.isdigit():
                currn += c
            elif c == "[":
                stack.append(
                    currs)  # only when necessary to put as preious string for storage, rpepare for new string in bracket
                stack.append(currn)  # record current num
                currs = currn = ""
            elif c == "]":
                currs *= int(stack.pop())  # get current state
                currs = stack.pop() + currs  # concatenate with prev, if any, else " ", as new current string as answer
            else:
                currs += c  # is string
        return currs

#         # method 2 ,
#         if not s: return ""
#         stack, num = [["", 1]], ""
#         for ch in s:
#             if ch.isdigit():
#                 num += ch
#             elif ch == '[':   # new recursive, create position with num
#                 stack.append(["", int(num)])
#                 num = ''
#             elif ch == ']':
#                 st, n = stack.pop()
#                 stack[-1][0] += st * n # str combine with rpevious

#             else:
#                 stack[-1][0] += ch
#         return stack[-1][0]


# not valid recursive method
# if not s: return ""
# tmp = []
# for char in s:
#     if char.islower():
#         tmp.append(char)
#     elif char.isdigit():
#         j = len(s)-s[::-1].index("]")
#         tmp.append(int(char) * self.decodeString(s[2:j]))
#         tmp.append(self.decodeString(s[j+1:]))
#         return "".join(tmp)
# return "".join(tmp)






