from api import APIClient
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

    response = client.get_endpoint1(params=params)
    pprint.pprint(response)

if __name__ == "__main__":
    main()