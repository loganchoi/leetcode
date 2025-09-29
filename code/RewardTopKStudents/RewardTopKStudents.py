class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        posWords = set(positive_feedback)
        negWords = set(negative_feedback)

        studentHeap = []

        for i in range(0,len(report)):
            curTotal = 0
            for word in report[i].split():
                if word in posWords:
                    curTotal += 3
                if word in negWords:
                    curTotal -= 1
            heapq.heappush(studentHeap, (-curTotal,student_id[i]))

        res = []
        while k != 0:
            curStudent = heapq.heappop(studentHeap)
            res.append(curStudent[1])
            k -=1
        
        return res