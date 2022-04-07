from . import db


class ScrapeModel(db.Model):
    id = db.Column('scrape_id', db.Integer, primary_key=True)
    url = db.Column(db.String(100))
    keyword = db.Column(db.String(50))
    time = db.Column(db.Float())
    load_time = db.Column(db.Float())
    hits = db.Column(db.Integer())

    def __init__(self, url, keyword, time, load_time, hits):
        self.url = url
        self.keyword = keyword
        self.time = time
        self.load_time = load_time
        self.hits = hits
