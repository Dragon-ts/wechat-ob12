import re
import json5
import datetime


class Notice:
    def __init__(self, description: str) -> None:
        pattern = r"datetime\.datetime\(.+\)"
        match = re.findall(pattern, description)[0]
        if len(match) == 0:
            self.description = json5.loads(description)
        else:
            self.description = json5.loads(description.replace(match, f"'{str(eval(match))}'"))
        self.user_id = self.description['user_id']
        self.group_id = self.description['group_id']
        self.time = self.description['time']
        self.type = self.description['detail_type']
        self.sender = self.description['from_user_id']
        self.self_id = self.description['self']['user_id']

    def get_user_id(self):
        return self.user_id

    def get_group_id(self):
        return self.group_id

    def is_tome(self) -> bool:
        return self.self_id == self.user_id
