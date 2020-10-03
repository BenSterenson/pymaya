class BadResponseException(Exception):
    def __init__(self, status_code, reason, url, method=None, *args) -> None:
        message = f"Bad response to URL: {url} in {method} method [status_code: {status_code}, reason: {reason}]"
        super(BadResponseException, self).__init__(message)
