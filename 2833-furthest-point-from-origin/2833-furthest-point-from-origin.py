class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count('L')
        right = moves.count('R')
        joker = moves.count('_')

        if len(moves) == 1: return 1 
        else: return max(abs(( left + joker) - right), abs(( right + joker) - left))