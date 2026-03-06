class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i=0

        # append all intervals preceeding new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        # modify new interval (merge overlaps)
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # add new interval
        output.append(newInterval)

        # add the rest 
        while i < len(intervals): 
            output.append(intervals[i])
            i += 1

        return output
