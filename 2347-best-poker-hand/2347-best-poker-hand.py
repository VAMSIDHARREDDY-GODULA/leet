class Solution(object):
    def bestHand(self, ranks, suits):
        if len(set(suits))==1: return 'Flush'
        elif len(set(ranks))==len(ranks): return 'High Card'
        b = []
        for i in set(ranks): b.append(ranks.count(i))
        return 'Pair' if max(b)==2 else 'Three of a Kind' 