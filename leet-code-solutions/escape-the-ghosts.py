class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mn= abs(ghosts[0][1] - target[1]) + abs(ghosts[0][0] - target[0])
        for i in ghosts:
            distance = abs(i[1] - target[1]) + abs(i[0] - target[0])
            mn = min(mn,distance)
        pacman = abs(0 - target[1]) + abs(0 - target[0])
        print(pacman, mn)
        if mn <= pacman:
            return False
        else:
            return True
