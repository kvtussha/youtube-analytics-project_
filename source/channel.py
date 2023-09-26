import json
from source.implemented import youtube


class Channel:
    youtube_api = youtube

    def __init__(self, channel_id):
        self._channel_id = channel_id
        self._channel = self.youtube_api.channels().list(id=channel_id, part='snippet,statistics').execute()

    def channel_item(self) -> dict | None:
        return self._channel.get('items')[0]

    def channel_snippet(self) -> dict | None:
        return self.channel_item().get('snippet')

    def channel_statistics(self) -> dict | None:
        return self.channel_item().get('statistics')

    @property
    def channel_id(self):
        return self._channel_id

    @property
    def title(self):
        return self.channel_snippet().get('title')

    @property
    def description(self):
        return self.channel_item().get('description')

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self._channel_id}"

    @property
    def subscriber_count(self):
        return self.channel_statistics().get('subscriberCount')

    @property
    def video_count(self):
        return self.channel_statistics().get('videoCount')

    @property
    def view_count(self):
        return self.channel_statistics().get('viewCount')

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """
        Выводит словарь в json-подобном удобном формате с отступами
        :return: словарь
        """
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self):
        """
        Метод возвращает информацио о канале
        :return: словарь с информацией
        """
        return self.printj(self._channel)

    @classmethod
    def get_service(cls):
        return cls.youtube_api

    def to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self._channel, f)

# moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# print(moscowpython.print_info())
