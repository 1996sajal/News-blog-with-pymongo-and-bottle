import urllib.request as ur
import urllib.error
import json
import bottle
import pymongo
import check_internet


class MongoConnect:

    def __init__(self):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        self.db = self.client["newster"]
        self.col = self.db["news"]
        print("Connecting to MongoDB : ", pymongo.get_version_string())

    def insert(self, news_data):
        for item in news_data:
            if self.col.find({"title": item["title"]}).count() == 0:
                self.col.insert_one(item)

    def find(self):
        return self.col.find().limit(-10)


def get_news(news_key):
    api_key = "6dd969d1d3a14e1bbf2f113ac5326549"
    response = ur.urlopen(" https://newsapi.org/v1/articles?source="+news_key+"&apiKey="+api_key)
    news_data = json.loads(response.read().decode("utf-8"))
    print(news_data["articles"][0].keys())
    return news_data


@bottle.route("/")
def start():
    return bottle.template("index.tpl")


@bottle.route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return bottle.static_file(filename, root='static/images/', mimetype='image/png')


@bottle.route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return bottle.static_file(filename, root='static/images/', mimetype='image/jpg')


@bottle.route('/<filename:re:.*\.css>')
def send_image(filename):
    return bottle.static_file(filename, root='static/')


@bottle.post("/")
def page():
    news_key = bottle.request.forms.get("name")
    print(news_key)
    connect = MongoConnect()
    if check_internet.is_connected():
        news_data = get_news(news_key)
        connect.insert(news_data["articles"])
        return bottle.template("interface.tpl", source=news_data["source"], articles=news_data["articles"])
    else:
        news_data = connect.find()
        return bottle.template("find.tpl", source=news_data)


def main():
    try:
        bottle.run(host="localhost", port=8080)
    except urllib.error.URLError:
        print("sajal")

if __name__ == '__main__':
    main()

