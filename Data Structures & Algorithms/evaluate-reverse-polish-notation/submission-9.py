class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = { "+", "-", "*", "/" }
        if len(tokens) == 1:
            if tokens[0] in symbols:
                return 0
            else:
                return int(tokens[0])

        stack = deque()
        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
                continue
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                match token:
                    case "+":
                        stack.append(num2 + num1)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num2 * num1)
                    case "/":
                        stack.append(int(num2 / num1))
                    case _:
                        pass
        return stack[-1]