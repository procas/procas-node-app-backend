class VideoResponse(object):
    status = ""
    message = ""
    url = ""

    def __init__(self, _status, _message, _url) -> None:
        self.status = _status
        self.message = _message
        self.url = _url
