class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        k = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and k < len(popped) and stack[-1] == popped[k]:
                stack.pop()
                k += 1

        return k == len(popped)