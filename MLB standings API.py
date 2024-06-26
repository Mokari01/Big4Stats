import requests

def fetch_mlb_standings(season):
    url = "https://api-baseball.p.rapidapi.com/standings"
    querystring = {"season": season, "league": "1"}  # Assuming '1' stands for MLB
    headers = {
        "X-RapidAPI-Key": "60ae690f03msh00322281f0bf93dp11feccjsn9c179c4d7da9",
        "X-RapidAPI-Host": "api-baseball.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    standings = response.json()
    print_mlb_standings(standings)

def print_mlb_standings(data):
    if data['results'] == 0:
        print("No standings found for the given season.")
        return

    print("MLB Standings:")
    for team_info in data['response'][0]:
        print(f"Position: {team_info['position']}, Team: {team_info['team']['name']}")
        print(f"Games Played: {team_info['games']['played']}, Wins: {team_info['games']['win']['total']}, Losses: {team_info['games']['lose']['total']}")
        print(f"Win Percentage: {team_info['games']['win']['percentage']}, Points For: {team_info['points']['for']}, Points Against: {team_info['points']['against']}")
        print(f"Form: {team_info['form']}")
        print("-" * 80)
