def tournamentWinner(competitions, results):

    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        # print(homeTeam, awayTeam)
        winningTeam = homeTeam if result == 1 else awayTeam

        UpdateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


def UpdateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]

tournamentWinner(competitions, results)
