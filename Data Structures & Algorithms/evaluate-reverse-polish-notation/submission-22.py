class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if (tokens[i] == "+"):
                tmp = int(stack[-2]) + int(stack[-1])
                # print(f"stack[-2] : {stack[-2]} , stack[-1] = {stack[-1]}")
                stack.pop()
                stack.pop()
                stack.append(str(tmp))
            elif (tokens[i] == "-"):
                tmp = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(tmp))
            elif (tokens[i] == "*"):
                tmp = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(tmp))
            elif (tokens[i] == "/"):
                # print(stack)
                print(f"stack[-2] : {stack[-2]} , stack[-1] = {stack[-1]}")
                tmp = int(int(stack[-2]) / int(stack[-1]))
                # if (abs(int(stack[-2])) < abs(int(stack[-1]))):
                #     tmp = 0
                print(tmp)
                stack.pop()
                stack.pop()
                stack.append(str(tmp))
            else :
                stack.append(tokens[i])
            # print(stack)

        return (int(stack[-1]))