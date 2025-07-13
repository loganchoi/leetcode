class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        pPtr = 0 
        tPtr = 0
        total = 0

        while pPtr < len(players) and tPtr < len(trainers):
            if players[pPtr] <= trainers[tPtr]:
                pPtr = pPtr + 1
                tPtr = tPtr + 1
                total = total + 1
            elif players[pPtr] > trainers[tPtr]:
                tPtr = tPtr + 1


        return total