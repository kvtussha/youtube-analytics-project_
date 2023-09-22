import json
from source.implemented import youtube


class Channel:

    def __init__(self, channel_id):
        self.channel_id = channel_id

    def printj(self, dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self):
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return self.printj(channel)

