class RegisterResponse(object):
    status = ""
    message = ""

    def __init__(self, _status, _message) -> None:
        self.status = _status
        self.message = _message
