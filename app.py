import json

class Constants:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            self.__dict__ = json.load(f)

        self.basic_price = {
            "name": "Basic Price",
            "value": self.IDpercent['value'] + self.TDpercent['value'] + 1
        }

