import requests
import json
from .configuration import constants
from flask import Response
from datetime import datetime, timedelta
import time
class Pocket:
    def __init__(self, request, config) -> None:
        self.request = request
        self.config = config


    def fetch_recent_items_from_pocket(self):
        try:
            last_hour_date_time = datetime.now() - timedelta(hours = 1)
            unix_timestamp = time.mktime(last_hour_date_time.timetuple())
            payload = json.dumps({
                        "consumer_key": self.config['consumer_key'],
                        "access_token": self.config['access_token'],
                        "since": unix_timestamp
                    })
            headers = {
                'Content-Type': 'application/json',
            }
            url = constants['get_data_from_pocket']
            response = requests.request("POST", url, headers=headers, data=payload)
            return response.json()
        except Exception as e:
            return e
