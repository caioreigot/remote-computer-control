from typing import List


class View_List():
    list: List


    def __init__(self) -> None:
        self.list = [
            App(),
            Close()
        ]


from .app.view import App
from .close.view import Close
