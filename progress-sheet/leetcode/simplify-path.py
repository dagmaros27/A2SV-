class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        i = 0
        while i < n - 1:
            if path[i] == "/":
                if i + 1 < n and (path[i + 1].isalnum() or path[i + 1] == "_" ):
                    word = "/"
                    j = 1
                    while i + j < n and (path[i + j] != '/'):
                        word += path[i + j]
                        j += 1
                    stack.append(word)
                    i += j-1

                elif i + 1 < n and path[i + 1] == "/":
                    j = 1
                    while i + j < n and path[i + j] == "/":
                        j += 1
                    print(j)
                    i += j - 2
                else:
                    periods = ""
                    j = 1
                    while i + j < n and path[i + j] != "/":
                        periods += path[i+j]
                        j += 1

                    if periods == ".." and stack:
                        stack.pop()
                    elif j > 3:
                        stack.append("/" + periods)
                    elif j ==3 and periods != "..":
                        stack.append("/" + periods)
                    i += j-2

            i += 1
        if not stack:
            return path[0]

        return "".join(stack)