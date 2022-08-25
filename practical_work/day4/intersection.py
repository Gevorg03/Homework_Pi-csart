class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect_lst = []
        for el in nums1:
            if el in nums2 and el not in intersect_lst:
                intersect_lst.append(el)
        return intersect_lst
