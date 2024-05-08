import requests

def fetch_nba_standings(season):
    url = "https://api-nba-v1.p.rapidapi.com/standings"
    querystring = {"league": "standard", "season": season}
    headers = {
        "X-RapidAPI-Key": "60ae690f03msh00322281f0bf93dp11feccjsn9c179c4d7da9",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    standings = response.json()
    print_nba_standings(standings)

def print_nba_standings(data):
    if data['results'] == 0:
        print("No standings found for the given season.")
        return

    print("NBA Standings:")
    print("-" * 80)
    for team in data['response']:
        print(f"Team: {team['team']['name']} ({team['team']['code']})")
        print(f"Conference: {team['conference']['name']}, Rank: {team['conference']['rank']}")
        print(f"Division: {team['division']['name']}, Rank: {team['division']['rank']}, Games Behind: {team['gamesBehind']}")
        print(f"Wins: Home: {team['win']['home']}, Away: {team['win']['away']}, Total: {team['win']['total']}")
        print(f"Losses: Home: {team['loss']['home']}, Away: {team['loss']['away']}, Total: {team['loss']['total']}")
        print(f"Winning Streak: {'Yes' if team['winStreak'] else 'No'}, Current Streak: {team['streak']} games")
        print("-" * 80)
