#!/usr/bin/env python3



from math import inf
import random



class TheGame:
    def __init__(self, player_id, minNegativeHP, maxNegativeHP):
        self.MIN = -inf
        self.MAX = inf
        self.depth = int(player_id[0]) * 2
        self.branching = int(player_id[2])
        self.initialHP = int(player_id[-2:][::-1])
        self.comparisonsAvoided = 0
        self.attacks = [random.randint(minNegativeHP, maxNegativeHP) for _ in range(pow(self.branching, self.depth))]  


    def run(self):
        self.bestAttack = self.AlphaBeta(0, 0, True, self.attacks, self.MIN, self.MAX) 
        print(f"Depth and Branches ratio is {self.depth}:{self.branching}")
        print(f"Terminal States (leaf node values) are {', '.join(map(str, self.attacks))}.")
        print(f"Left life(HP) of the defender after maximum damage caused by the attacker is {self.initialHP - self.bestAttack}")
        print(f"After Alpha-Beta Pruning Leaf Node Comparisons {len(self.attacks) - self.comparisonsAvoided}")
        

    def AlphaBeta(self, depth, nodeIndex, maximizingPlayer, values, alpha, beta): 
        if depth == self.depth: 
            return values[nodeIndex] 
    
        if maximizingPlayer: 
    
            maxEval = self.MIN
    
            for i in range(0, self.branching): 
    
                val = self.AlphaBeta(depth + 1, nodeIndex * self.branching + i, False, values, alpha, beta) 
                maxEval = max(maxEval, val) 
                alpha = max(alpha, val) 
    
                if beta <= alpha: 
                    self.comparisonsAvoided += ((pow((self.branching), (self.depth - depth - 1))) * (self.branching - i - 1))
                    break

            return maxEval 
    
        else:

            minEval = self.MAX
    
            for i in range(0, self.branching): 
    
                val = self.AlphaBeta(depth + 1, nodeIndex * self.branching + i, True, values, alpha, beta) 
                minEval = min(minEval, val) 
                beta = min(beta, val) 
    
                if beta <= alpha: 
                    self.comparisonsAvoided += ((pow((self.branching), (self.depth - depth - 1))) * (self.branching - i - 1))
                    break
    
            return minEval 
    


if __name__ == "__main__": 

    player_id = input()
    minNegativeHP, maxNegativeHP = list(map(int, input().split()))

    TheGame(player_id, minNegativeHP, maxNegativeHP).run()
