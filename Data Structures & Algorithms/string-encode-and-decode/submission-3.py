class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = [str(len(string)) + "#" + string for string in strs]
        return "".join(coded)

    def decode(self, s: str) -> List[str]:
        
        out = []

        i = 0

        while i < len(s):

            j = i
            while s[j] != '#':    # find the '#'
                    j += 1

            length = int(s[i:j])  # length string from i to j
            i = j + 1             # move past '#'
            j = i + length        # end of the string
            out.append(s[i:j])
            i = j
            
        return out