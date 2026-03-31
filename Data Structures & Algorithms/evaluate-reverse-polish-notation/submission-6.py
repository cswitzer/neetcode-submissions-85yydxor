class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        if len(tokens) == 1:
            if tokens[0] in operators:
                return 0
            else:
                return int(tokens[0])
        
        stack = []
        for token in tokens:
            if token not in operators:
                # must be a number in this case
                stack.append(int(token))
                print(f"stack state <number>: {str(stack)}")
            else:
                match token:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "-":
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(stack.pop() * stack.pop())
                    case "/":
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(int(num1 / num2))
                    case _:
                        pass
                print(f"stack state <token>: {str(stack)}")

        return stack[-1]
