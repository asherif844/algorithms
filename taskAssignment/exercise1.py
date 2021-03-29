def taskAssignment(k, tasks):
    indexSearch = getTaskIndex(tasks)
    sortedTasks = sorted(tasks)
    finalTasks = []

    rightIdx = len(sortedTasks) - 1
    leftIdx = 0

    while leftIdx < rightIdx:
        leftTaskDuration = sortedTasks[leftIdx]
        leftTaskIndex = indexSearch[leftTaskDuration]
        leftTask = leftTaskIndex.pop()
        leftIdx += 1

        rightTaskDuration = sortedTasks[rightIdx]
        rightTaskIndex = indexSearch[rightTaskDuration]
        rightTask = rightTaskIndex.pop()
        rightIdx -= 1

        finalTasks.append([leftTask, rightTask])

    return finalTasks


def getTaskIndex(tasks):
    taskTable = {}
    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskTable:
            taskTable[taskDuration].append(idx)
        else:
            taskTable[taskDuration] = [idx]
    return taskTable


k = 3
tasks = [1, 3, 5, 3, 1, 4]
taskAssignment(k, tasks)
# getTaskIndex(tasks)
