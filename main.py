from api import APIClient
from endpoints.games import GamesEndpoint
import pprint

def main():
    games_base_url = "https://api.rawg.io/api"
    headers = {}

    client = APIClient(games_base_url, headers=headers)
    games_endpoint = GamesEndpoint(client)

    params = {
        "page": 1,
        "page_size": 1,
        "key": "5d9f1b5510dc47f69480887ec649dccb"
    }

    # Use pagination from GamesEndpoint
    all_games = games_endpoint.get_games(params=params)

    pprint.pprint(all_games)

if __name__ == "__main__":
    main()
