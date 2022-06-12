class Note(object):
    title = ""
    detail = ""
    date = ""

    def __init__(self, title, detail, date) -> None:
        self.title = title
        self.detail = detail
        self.date = date
