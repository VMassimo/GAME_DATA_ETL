from api import APIClient
from endpoints.games import GamesEndpoint 
import pprint 



def main():
    base_url = "https://api.rawg.io/api"
    headers = {}

    client = APIClient(base_url,headers=headers)

    params = {
        "page":1,
        "page_size": 1,
        "key": "5d9f1b5510dc47f69480887ec649dccb"
    }

    games_endpoint = GamesEndpoint(client)

    response = games_endpoint.get_games(params=params)
    pprint.pprint(response)

if __name__ == "__main__":
    main()