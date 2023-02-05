from notionwrapper.notion_wrapper import Notion
from configuration import config
from flask import Flask, request

app = Flask(__name__)

@app.route("/",methods = ['GET'])
def healthcheck():
    return {"message": "OK"}

@app.route("/pocket-to-notion",methods = ["POST"])
def pocket_to_notion():
    notion = Notion(request.json,config)
    return notion.create_page_in_notion()

if __name__ == "__main__":
    print('This is Running')
    app.run(host="localhost",port = 3000,debug=config['debug'])
