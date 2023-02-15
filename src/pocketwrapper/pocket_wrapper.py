"""
Main Method for Our Pocket API Wrapper
"""
import requests
import json
from .configuration import constants
from datetime import datetime, timedelta
import time


class Pocket:
    """
    Pocket Class to Handle Interaction with the Pocket API
    """

    def __init__(self, request, config) -> None:
        self.request = request
        self.config = config

    def fetch_recent_items_from_pocket(self):
        try:
            last_hour_date_time = datetime.now() - timedelta(hours=1)
            unix_timestamp = time.mktime(last_hour_date_time.timetuple())
            payload = json.dumps({
                "consumer_key": self.config["consumer_key"],
                "access_token": self.config["access_token"],
                "since": unix_timestamp
            })
            headers = {
                "Content-Type": "application/json",
            }
            print(payload)
            url = constants["get_data_from_pocket"]
            response = requests.request(
                "POST", url, headers=headers, data=payload, timeout=5)
            return response.json()
        except Exception as e:
            return e
