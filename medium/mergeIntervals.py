# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    i=0
    while(i!=len(intervals)-1):
        if (intervals[i+1][0]) in range(intervals[i][0],intervals[i][1]+1):
            x=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i+1][1],intervals[i][1])]
            intervals.pop(i+1)
            intervals.pop(i)
            intervals.insert(i,x)
        else:
            i+=1
    return(intervals)