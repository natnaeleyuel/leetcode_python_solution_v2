class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        l1 = [s1[i] for i in range(len(s1)) if i % 2 == 0]
        l2 = [s1[i] for i in range(len(s1)) if i % 2 == 1]
        l3 = [s2[i] for i in range(len(s2)) if i % 2 == 0]
        l4 = [s2[i] for i in range(len(s2)) if i % 2 == 1]
        l1.sort()
        l2.sort()
        l3.sort()
        l4.sort()

        if "".join(l1) == "".join(l3):
            if "".join(l2) == "".join(l4):
                return True

        return False