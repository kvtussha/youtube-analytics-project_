class IdValueError(Exception):
    def __init__(self, message='Такого id видео не существует'):
        super().__init__(message)
        self._video = None
        self.title = None
        self.link = None
        self.view_count = None
        self.like_count = None
        self.duration = None
