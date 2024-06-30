import aiohttp
import asyncio
import json

async def get_access_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status == 200:
                return await response.json()
            else:
                error_message = await response.text()
                raise Exception(f"Error obtaining access token: {response.status} - {error_message}")

async def search_games(query):
    with open('config.json', 'r') as f:
        config = json.load(f)
        
    client_id = config['client_id']
    client_secret = config['client_secret']
    
    access_token_response = await get_access_token(client_id, client_secret)
    access_token = access_token_response['access_token']
    
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }

    body = f"""
    fields id, name, cover.url;
    search "{query}";
    limit 10;
    """

    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.igdb.com/v4/games/', headers=headers, data=body) as response:
            if response.status == 200:
                return await response.json()
            else:
                error_message = await response.text()
                raise Exception(f"Error: {response.status} - {error_message}")

async def get_game_details(game_id):
    with open('config.json', 'r') as f:
        config = json.load(f)
        
    client_id = config['client_id']
    client_secret = config['client_secret']
    
    access_token_response = await get_access_token(client_id, client_secret)
    access_token = access_token_response['access_token']
    
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }

    body = f"""
    fields name, cover.url, platforms.name;
    where id = {game_id};
    """

    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.igdb.com/v4/games/', headers=headers, data=body) as response:
            if response.status == 200:
                games = await response.json()
                if games:
                    return games[0]
                else:
                    raise Exception(f"No game found with ID {game_id}")
            else:
                error_message = await response.text()
                raise Exception(f"Error: {response.status} - {error_message}")
