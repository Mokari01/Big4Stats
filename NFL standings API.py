import requests

def fetch_nfl_standings(year):
    url = "https://api-american-football.p.rapidapi.com/standings"
    querystring = {"league": "1", "season": year}
    headers = {
        "X-RapidAPI-Key": "60ae690f03msh00322281f0bf93dp11feccjsn9c179c4d7da9",
        "X-RapidAPI-Host": "api-american-football.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    standings = response.json()
    print_nfl_standings(standings)

def print_nfl_standings(data):
    if 'response' in data and len(data['response']) > 0:
        print("NFL Standings:\n")
        for team in data['response']:
            print(f"{team['team']['name']} - Conference: {team['conference']}, Division: {team['division']}")
            print(f"Position: {team['position']}, Wins: {team['won']}, Losses: {team['lost']}, Ties: {team['ties']}")
            print(f"Points For: {team['points']['for']}, Points Against: {team['points']['against']}, Point Difference: {team['points']['difference']}")
            print(f"Home Record: {team['records']['home']}, Road Record: {team['records']['road']}")
            print(f"Conference Record: {team['records']['conference']}, Division Record: {team['records']['division']}")
            print(f"Current Streak: {team['streak']}\n")
            print("-" * 80)
    else:
        print("No standings available for the given season.")
