class LoginResponse(object):
    status = ""
    message = ""
    token = ""

    def __init__(self, _status, _message, _token) -> None:
        self.status = _status
        self.message = _message
        self.token = _token
