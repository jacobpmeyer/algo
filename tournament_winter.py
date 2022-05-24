def tournamentWinner(competitions, results):
  """
  create a points dictionary where each key is a team
  iterate over each competition, adding the team key when needed and giving 3 points to the winning team.
  iterate over the dictionary to find the team with the highest score, keeping track of highest score and team with score in a local array.
  """
  currentLeader = "teamPlaceholder"
  teams = {currentLeader: -1}
  for i, comp in enumerate(competitions):
    # comp is formatted as [homeTeam(1), awayTeam(0)]
    homeTeam, awayTeam = comp

    winner = homeTeam if results[i] == 1 else awayTeam

    updateTeamScore(winner, teams)

    if teams[winner] > teams[currentLeader]:
      currentLeader = winner

  return currentLeader

def updateTeamScore(team, teams):
  if team not in teams:
    teams[teams] = 0

  teams[team] += 3
