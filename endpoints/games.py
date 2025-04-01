from api import APIClient

class GamesEndpoint():
    def __init__(self, client: APIClient):
        self.client = client

    def get_games(self, params):
        """
        Example: GET request to an endpoint.
        """
        endpoint = "/games"
        return self.client._make_request("GET", endpoint, params=params) 

# def post_endpoint2(self, data):
#     """
#     Example: POST request to an endpoint.
#     """
#     endpoint = "/endpoint2"
#     return self._make_request("POST", endpoint, json=data)