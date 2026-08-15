class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = 0
        prevPos = 0
        for i in range(len(requests)):
            curPos = requests[i]
            travel = abs(curPos - prevPos)
            time += travel
            prevPos = curPos
        return time