"""
Main Method for Our API
"""
from configuration import config
from middlewares.rate_limiter import rate_limiting_logic
from middlewares.print_logs import print_log
from flask import Flask, request
from datetime import datetime, timedelta
from notionwrapper.notion_wrapper import Notion
from pocketwrapper.pocket_wrapper import Pocket

app = Flask(__name__)


@app.route("/", methods=["GET"])
@rate_limiting_logic()
def healthcheck():
    return {"message": "OK"}


@app.route("/pocket-to-notion", methods=["POST"])
@rate_limiting_logic()
def pocket_to_notion():
    notion = Notion(request.json, config)
    return notion.create_page_in_notion()


@app.route("/callback-url", methods=["GET"])
def callback_function():
    return """<html>Success</html>"""


@app.route("/fetch-pocket-data", methods=["POST"])
@print_log()
def fetch_pocket_data():
    last_hour_date_time = datetime.now() - timedelta(hours=1)
    print(last_hour_date_time.strftime("%Y-%m-%d %H:%M:%S"))
    pocket = Pocket(request.get_json(force=True), config)
    return pocket.fetch_recent_items_from_pocket()


if __name__ == "__main__":
    print("This is Running")
    app.run(host="0.0.0.0", port=config["port"], debug=False)
