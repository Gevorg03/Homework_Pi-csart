class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        lst = []
        for i in range(1, target[-1] + 1):
            if i in target:
                lst.append("Push")
            else:
                lst.append("Push")
                lst.append("Pop")
        return lst
