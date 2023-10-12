import json

from source.implemented import youtube


class Video:
    youtube_api = youtube

    def __init__(self, video_id):
        self.video_id = video_id
        self._video = self.youtube_api.videos().list(id=video_id, part='snippet,contentDetails,'
                                                                       'statistics,status').execute()

    def __str__(self):
        return str(self.title)

    def item(self):
        return self._video.get("items")[0]

    def snippet(self) -> dict | None:
        return self.item().get('snippet')

    def statistics(self) -> dict | None:
        return self.item().get('statistics')

    def content_details(self) -> dict | None:
        return self.item().get('contentDetails')

    @property
    def id(self):
        return self.video_id

    @property
    def title(self):
        return self.snippet().get('title')

    @property
    def link(self):
        return f"https://www.youtube.com/watch?v={self.id}"

    @property
    def view_count(self):
        return self.statistics().get('viewCount')

    @property
    def like_count(self):
        return self.statistics().get('likeCount')

    @property
    def duration(self):
        return self.content_details().get('duration')

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """
        Выводит словарь в json-подобном удобном формате с отступами
        :return: словарь
        """
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self):
        """
        Метод возвращает информацию о канале
        :return: словарь с информацией
        """
        return self.printj(self._video)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id


# video1 = Video('feg3DYywNys')
# print(video1.print_info())
