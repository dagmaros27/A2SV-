class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = list()
        for log in logs:
            if log == "../":
                if len(stack) > 0:
                    stack.pop()
            elif log == "./":
                pass
            else:
                stack.append(log)
        return len(stack)

        