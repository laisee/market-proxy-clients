import requests

from utils.access_token import generate_access_token


def query_balances(cfg, version="v1"):
    ENDPOINT = "/{}/api/balances".format(version)
    token = generate_access_token(cfg["api_key"], cfg["private_key"])
    headers = {'credentials_secret': token}
    return requests.get(cfg["http_url"] + ENDPOINT, headers=headers)