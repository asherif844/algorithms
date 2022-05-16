
intervals = [[1, 2], [4, 7], [3, 5], [6, 8], [9, 10]]


def mergeOverlappingIntervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in sorted_intervals:
        current_first_interval, current_last_interval = current_interval
        next_first_interval, next_last_interval = next_interval

        if current_last_interval >= next_first_interval:
            current_interval[1] = max(
                next_last_interval, current_last_interval)
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals


mergeOverlappingIntervals(intervals)
