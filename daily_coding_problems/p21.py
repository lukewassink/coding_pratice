# Given an array of time intervals (start, end) for classroom lectures
# (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def maxOverlap(intervals):
    if not intervals:
        return 0

    intervals.sort()

    maxOverlap = 1
    left = 0
    right = 0

    while right < len(intervals):
        x1, y1 = intervals[left]
        x2, y2 = intervals[right]
        if x2 <= y1:
            right += 1
        else:
            left += 1
        maxOverlap = max(maxOverlap, right - left)

    return maxOverlap

print(maxOverlap([(30, 75), (0, 50), (60, 150)]))
