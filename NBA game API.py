import requests

def fetch_nba_games(date):
    url = "https://api-nba-v1.p.rapidapi.com/games"
    querystring = {"date": date}
    headers = {
        "X-RapidAPI-Key": "60ae690f03msh00322281f0bf93dp11feccjsn9c179c4d7da9",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    games = response.json()
    print_nba_games(games)

def print_nba_games(data):
    if data['results'] == 0:
        print("No games found for the given date.")
        return

    print("NBA Game Results:")
    print("-" * 100)
    for game in data['response']:
        print(f"Date: {game['date']['start'][:10]}")
        print(f"Arena: {game['arena']['name']}, {game['arena']['city']}, {game['arena']['state']}")
        print(f"Visiting Team: {game['teams']['visitors']['name']} - Points: {game['scores']['visitors']['points']}")
        print(f"Home Team: {game['teams']['home']['name']} - Points: {game['scores']['home']['points']}")
        print("Score by Quarter (Visitors - Home):")
        for v_score, h_score in zip(game['scores']['visitors']['linescore'], game['scores']['home']['linescore']):
            print(f"{v_score} - {h_score}")
        print("-" * 100)
