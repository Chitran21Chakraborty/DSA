class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals based on their start times
        intervals.sort(key = lambda i : i[0])
        
        # Step 2: Initialize output list with the first interval
        output = [intervals[0]]
        
        # Step 3: Iterate through the remaining intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            # If current interval overlaps with the last one, merge them
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # Otherwise, add it as a new separate interval
            else:
                output.append([start, end])
                
        return output