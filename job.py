import json


class job:
    def __init__(self, jobInJson):
        self._name = jobInJson["name"]
        self._current_status = jobInJson["color"]
        self._url = jobInJson["url"]

    def get_name(self):
        return self._name

    def get_status(self):
        return self._current_status

    def update_status(self, status):
        self._current_status = status

    def get_url(self):
        return self._url