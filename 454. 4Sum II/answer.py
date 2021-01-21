def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    from collections import Counter
    sum_dict = Counter([a + b for a in A for b in B ])
    return sum(sum_dict[-c-d] for c in C for d in D)
