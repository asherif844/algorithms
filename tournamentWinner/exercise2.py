import json


def tournamentWinner(competitions, results):
    bestTeam = ""
    scores = {bestTeam: 0}

    for idx, competition in enumerate(competitions):
        homeTeam, awayTeam = competition
        result = results[idx]

        winningTeam = homeTeam if result == 1 else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[bestTeam]:
            bestTeam = winningTeam

        return bestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


with open('data.json', 'r') as f:
    data = json.load(f)


competitions = data['competitions']
results = data['results']

tournamentWinner(competitions, results)
