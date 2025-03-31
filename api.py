import requests
import pprint


class APIClient:
    def __init__(self, base_url, headers=None):
        """
        Initialize the API client with a base URL and optional headers.
        """
        self.base_url = base_url
        self.headers = headers or {}

    def _make_request(self, method, endpoint, params=None, data=None, json=None):
        """
        Private method to handle API requests and print the full URL.
        """
        # Construct the URL with the base URL and endpoint
        url = f"{self.base_url}{endpoint}"

        # If parameters are provided, append them as query parameters
        if params:
            from urllib.parse import urlencode
            url += "?" + urlencode(params)

        # Print the full URL
        print(f"Full URL: {url}")

        try:
            # Make the API request
            response = requests.request(
                method, url, headers=self.headers, params=params, data=data, json=json
            )
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Request failed: {e}")
            return None

    def get_games(self, params):
        """
        Example: GET request to an endpoint.
        """
        endpoint = "/games"
        params = params
        return self._make_request("GET", endpoint, params=params)

    def post_endpoint2(self, data):
        """
        Example: POST request to an endpoint.
        """
        endpoint = "/endpoint2"
        return self._make_request("POST", endpoint, json=data)

    # def get_paginated_data(self, endpoint, limit=100):
    #     """
    #     Example: Handling pagination automatically.
    #     """
    #     all_data = []
    #     offset = 0

    #     while True:
    #         params = {"limit": limit, "offset": offset}
    #         response = self._make_request("GET", endpoint, params=params)
    #         if not response:
    #             break

    #         all_data.extend(response.get("results", []))
    #         if len(response.get("results", [])) < limit:
    #             break  # Exit loop if we retrieved less than the limit

    #         offset += limit

    #     return all_data
