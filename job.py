import json


class job:
    def __init__(self, jobInJson):
        self._name = jobInJson["name"]
        self._current_status = jobInJson["color"]
        self._url = jobInJson["url"]