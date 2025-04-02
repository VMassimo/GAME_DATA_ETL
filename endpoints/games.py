from api import APIClient
import logging

logger = logging.getLogger(__name__)

class GamesEndpoint:
    def __init__(self, client: APIClient):
        self.client = client

    def get_games(self, params=None, id = None):
        """
        Fetch a single page of games.
        """
        if id is not None:
            endpoint = f"/games/{id}"
        else:
            endpoint = "/games"
        return self.client._make_request("GET", endpoint, params=params)

    def get_all_games(self, params):
        """
        Fetch all games using pagination.
        """
        all_games = []
        page = 1
        page_size = params.get("page_size", 50)

        while True:
            params["page"] = page
            response = self.get_games(params=params)

            if not response or "results" not in response:
                break

            all_games.extend(response["results"])

            if len(response["results"]) < page_size:
                break  # Stop if we received less than page_size, meaning no more data.

            page += 1

        logger.info(f"Retrieved {len(all_games)} total games.")
        return all_games
