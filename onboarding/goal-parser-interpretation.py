class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        word = ""

        while i < len(command):
            if command[i] == 'G':
                word += "G"
            elif command[i] == '(':  
                if command[i+1] == ')':
                    word += "o"
                    i += 1
                elif command[i+1] == 'a':
                    word += "al"
                    i += 2
            i += 1
        return word
            