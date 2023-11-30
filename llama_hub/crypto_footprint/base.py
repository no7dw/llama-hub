import requests
import urllib.parse

from typing import Dict, List, Optional

from llama_index.readers.base import BaseReader
from llama_index.readers.schema.base import Document


class CryptoReader(BaseReader):

    def __init__(self, api_key: str):
        """
        https://docs.footprint.network/docs
        Args:
            api_key:
        """
        self.api_key = api_key
        self.headers = {
            "accept": "application/json",
            "api-key": api_key  # "demo-api-key"
        }

    def load_data(self, domain, query_dict: Dict = None, sort_key: str = "", direction: str = "", limit: int = 100,
                  offset: int = 0) -> List[Document]:
        """

        Args:
            domain: example:
                url = "https://api.footprint.network/api/v3/address/getWalletERC20TokenBalance?chain=Ethereum&wallet_address=0x46efbaedc92067e6d60e84ed6395099723252496"
                then domain should be 'address/getWalletERC20TokenBalance'
            query_dict:
            sort_key:
            direction:
            limit:
            offset:

        Returns:

        """

        query_string = urllib.parse.urlencode(query_dict)
        url = f"https://api.footprint.network/api/v3/{domain}?{query_string}"

        response = requests.get(url, headers=self.headers)
        return [Document(text=str(data)) for data in response]


if __name__ == "__main__":
    cr = CryptoReader(api_key="demo-api-key")
    # url = "https://api.footprint.network/api/v3/address/getWalletERC20TokenBalance?chain=Ethereum&wallet_address" \
    #       "=0x46efbaedc92067e6d60e84ed6395099723252496"
    query_dict = {'chain': 'Ethereum',
                  'wallet_address': '0xa25a9b7c73158b3b34215925796ce6aa8100c13a',
                  'limit': 3,
                  'token_address': '0x6b3595068778dd592e39a122f4f5a5cf09c90fe2'
                  }
    res = cr.load_data(domain='address/getWalletERC20TokenBalance', query_dict=query_dict)
    print(res)
