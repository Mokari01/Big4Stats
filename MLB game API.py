import requests
from datetime import datetime

def fetch_mlb_games(date):
    year = datetime.strptime(date, '%Y-%m-%d').year  # Extract the year from the date
    url = "https://api-baseball.p.rapidapi.com/games"
    querystring = {"date": date, "season": str(year), "league": "1"}  # Use the extracted year for season
    headers = {
        "X-RapidAPI-Key": "60ae690f03msh00322281f0bf93dp11feccjsn9c179c4d7da9",
        "X-RapidAPI-Host": "api-baseball.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    games = response.json()
    print_mlb_games(games)

def print_mlb_games(game_data):
    games = game_data.get('response', [])
    for game in games:
        date_time = game['date']
        home_team = game['teams']['home']['name']
        away_team = game['teams']['away']['name']
        home_score = game['scores']['home']['total']
        away_score = game['scores']['away']['total']
        status = game['status']['long']

        print(f"Date & Time: {date_time}")
        print(f"Match: {home_team} vs {away_team}")
        print(f"Score: {home_team} {home_score} - {away_team} {away_score}")
        print(f"Status: {status}")
        print("-" * 40)  # Separator for readability
