import requests
from datetime import datetime

def fetch_nfl_games(date):
    year = datetime.strptime(date, '%Y-%m-%d').year
    url = "https://api-american-football.p.rapidapi.com/games"
    querystring = {"date": date, "season": str(year), "league": "1"}
    headers = {
        "X-RapidAPI-Key": "60ae690f03msh00322281f0bf93dp11feccjsn9c179c4d7da9",
        "X-RapidAPI-Host": "api-american-football.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    games = response.json()
    print_games(games)

def print_games(data):
    # Check if 'response' key is in the data and has content
    if 'response' in data and len(data['response']) > 0:
        # Loop through each game in the response
        for game_info in data['response']:
            # Extract game and teams information
            game = game_info['game']
            teams = game_info['teams']
            scores = game_info['scores']

            # Print game information
            print(f"Game ID: {game['id']} - {teams['home']['name']} vs {teams['away']['name']}")
            print(f"Date: {game['date']['date']} Time: {game['date']['time']} at {game['venue']['name']}")
            print(f"Score: {teams['home']['name']} {scores['home']['total']} - {teams['away']['name']} {scores['away']['total']}")
            print(f"Status: {game['status']['long']}")
            print("\n")
    else:
        print("No game data available.")
