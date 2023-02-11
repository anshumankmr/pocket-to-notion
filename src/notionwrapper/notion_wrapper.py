"""
Notion Wrapper Function Class
"""
import requests
import json
from .configuration import constants


class Notion:
    """
    Notion Wrapper Library
    """

    def __init__(self, request, config) -> None:
        self.request = request
        self.config = config

    def create_page_in_notion(self):
        try:
            payload = json.dumps({
                "parent": {
                    "database_id": self.request["database_id"]
                },
                "properties": {
                    "Type": {
                        "select": {
                            "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                            "name": "Article",
                            "color": "default"
                        }
                    },
                    "Name": {
                        "title": [
                            {
                                "text": {
                                    "content": self.request["title"]
                                }
                            }
                        ]
                    },
                    "Link": {
                        "url": self.request["link"]
                    }
                }
            })
            api_key = self.config["notion_key"]
            headers = {
                "Content-Type": "application/json",
                "Notion-Version": "2022-02-22",
                "Authorization": f"Bearer {api_key}",
            }
            url = constants["create_page_id"]
            # print(api_key, url, headers, payload)
            response = requests.request("POST", url, headers=headers,
                                        data=payload, timeout=5)
            # print(response.text)
            return {"message": "OK"}
        except Exception as e:
            return e
