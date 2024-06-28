import requests
import json

def get_access_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Error obtaining access token: {response.status_code}")

def search_games(query):
    with open('config.json', 'r') as f:
        config = json.load(f)
        
    client_id = config['client_id']
    client_secret = config['client_secret']
    
    access_token = get_access_token(client_id, client_secret)
    
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }

    body = f"""
    fields name, cover.url;
    search "{query}";
    limit 10;
    """

    response = requests.post('https://api.igdb.com/v4/games/', headers=headers, data=body)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}")
