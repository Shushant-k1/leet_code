
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        from queue import PriorityQueue 
        q = PriorityQueue()
        for i in range(len(classes)):
            imp = (classes[i][0] + 1) / (classes[i][1] + 1) - classes[i][0] / classes[i][1]
            q.put((-imp, i))
        for i in range(extraStudents):
            imp, ind = q.get()
            classes[ind][0] += 1
            classes[ind][1] += 1
            imp = (classes[ind][0] + 1) / (classes[ind][1] + 1) - classes[ind][0] / classes[ind][1]
            q.put((-imp, ind))

        total_ratio = 0
        for passed, total in classes:
            total_ratio += passed / total
        
        return total_ratio / len(classes)
