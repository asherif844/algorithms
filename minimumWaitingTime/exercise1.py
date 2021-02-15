queries = [3, 2, 1, 2, 6]
def minimumWaitingTime(queries):
    waitingTime = []
    if len(queries) ==1:
        return 0
            
    queries = sorted(queries)
    waiting = 0
    for i in range(0, len(queries)):
        waiting = queries[:i]
        waiting = sum(waiting)
        waitingTime.append(waiting)
     
    return sum(waitingTime) 



minimumWaitingTime(queries)