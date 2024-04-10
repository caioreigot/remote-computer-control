from flask.views import View as FlaskView
from flask import Response
from typing import List
from .get.get import Get


class Close(FlaskView):
    rota: str = '/close'
    methods: List[str] = ['get']
    name: str = __name__

    
    def dispatch_request(self) -> Response:
        return self.get()


    def get(self):
        return Get().handle_request()
