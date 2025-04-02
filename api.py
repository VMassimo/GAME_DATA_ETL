import requests
import logging
from urllib.parse import urlencode

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url, headers=None):
        """
        Initialize the API client with a base URL and optional headers.
        """
        self.base_url = base_url
        self.headers = headers or {}

    def _make_request(self, method, endpoint, params=None, data=None, json=None):
        """
        Private method to handle API requests and log the full URL.
        """
        url = f"{self.base_url}{endpoint}"

        if params:
            url += "?" + urlencode(params)

        logger.info(f"Making {method} request to: {url}")

        try:
            response = requests.request(
                method, url, headers=self.headers, params=params, data=data, json=json
            )
            response.raise_for_status()
            logger.info(f"Response received: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API Request failed: {e}")
            return None
        
